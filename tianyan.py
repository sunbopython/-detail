from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def driver_open():
	dcap = dict(DesiredCapabilities.PHANTOMJS)
	dcap["phantomjs.page.settings.userAgent"] = (
		"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36"
		)
	driver = webdriver.PhantomJS(executable_path='D:/phantomjs-2.1.1-windows/bin/phantomjs.exe',desired_capabilities=dcap)
	return driver

def get_content(driver,url):
	driver.get(url)
	time.sleep(5)
	content = driver.page_source.encode('utf-8')
	driver.close()
	soup = BeautifulSoup(content, 'lxml')
	return soup

def get_basic_info(soup):
	company = soup.select('div.company_header_width > div > span')[0].text.replace('\n','').replace(" ","")
	fddbr = soup.select('div.company-human-box > div.human-top > div > div > a')[0].text
	zczb = soup.select('div.new-border-bottom > div.pb10 > div')[0].text.replace("\n","").replace(" ","")
	zt = soup.select('div.pt10 > div > div.statusType1')[0].text.replace("\n","").replace(" ","")
	zcrq = soup.select('div.pt10 > div.pb10 > div.baseinfo-module-content-value')[0].text.replace("\n","").replace(" ","")
	basics = soup.select('div.base2017 > table > tbody > tr')
	hy = basics[3].select('td > div > span')[0].text
	qyzch = basics[0].select('td > div > span')[0].text
	qylx = basics[1].select('td')[1].select('div > span')[0].text
	zzjgdm = basics[0].select('td')[1].select('div > span')[0].text
	yyqx = basics[3].select('td')[1].select('div > span')[0].text.replace("\n","").replace(" ","")
	djjg = basics[4].select('td')[1].select('div > span')[0].text
	hzrq = basics[4].select('td > div > span')[0].text
	tyshxydm = basics[1].select('td')[1].select('div > span')[0].text
	zcdz = basics[5].select('td > div > span')[0].text
	jyfw = basics[6].select('td > div > span > span > span')[0].text
	print(u'公司名称        : ' + company)
	print(u'法定代表人      : ' + fddbr)
	print(u'注册资本        : ' + zczb)
	print(u'公司状态        : ' + zt)
	print(u'注册日期        : ' + zcrq)
	print(u'行业            : ' + hy)
	print(u'工商注册号      : ' + qyzch)
	print(u'企业类型        : ' + qylx)
	print(u'组织机构代码    : ' + zzjgdm)
	print(u'营业期限        : ' + yyqx)
	print(u'登记机构        : ' + djjg)
	print(u'核准日期        : ' + hzrq)
	print(u'统一社会信用代码: ' + tyshxydm)
	print(u'注册地址        : ' + zcdz)
	print(u'经营范围        : ' + jyfw)

def get_gg_info(soup):
	ggpersons = soup.select('div.clearfix > div.staffinfo-module-container > div > a')
	ggnames = soup.select('div.clearfix > div.staffinfo-module-container > div > div > span')
	for i in range(len(ggpersons)):
		ggperson = ggpersons[i].text
		ggname = ggnames[i].text
		print(ggperson+'-------'+ggname)
	
def get_gd_info(soup):
	sel = soup.select('div#_container_holder > div > table.companyInfo-table > tbody > tr')
	for info in sel:
		name = info.select('td > a')[0].text.replace('\n','').replace(" ","")
		company_numl = info.select('td > div > a')[0].text.replace(' ','').replace('>','')
		percentage = info.select('td')[1].select('div > div > span')[0].text
		money = info.select('td')[2].select('div > span')[0].text
		data = info.select('td')[2].select('div > span')[1].text
		print(name+ ' :' + company_numl+ ', ' + '出资比例:' +percentage +', '+ money+', '+data)



def get_tz_info(soup):
	sel = soup.select('div.out-investment-container > table.companyInfo-table > tbody > tr')
	for info in sel:	
		company_name = info.select('td')[0].select('a > span')[0].text
		person_name = info.select('td')[1].select('span')[0].select('a')[0].text.replace('\n','').replace(" ","")
		company_numl = info.select('td')[1].select('span')[1].select('a')[0].text.replace(' ','').replace('>','')
		add_money = info.select('td')[2].select('span')[0].text
		touzi_num = info.select('td')[3].select('span')[0].text
		touzi_persent = info.select('td')[4].select('span')[0].text
		touzi_data = info.select('td')[5].select('span')[0].text
		zhuangtai = info.select('td')[6].select('span')[0].text.replace('\n','').replace(" ","")
		print(company_name+' '+person_name+':'+company_numl+' 注册：'+add_money+touzi_num+touzi_persent+touzi_data+' 状态：'+zhuangtai)

if __name__ == '__main__':

	url = 'http://www.tianyancha.com/company/2310290454'
	driver = driver_open()
	soup = get_content(driver,url)
	print('----获取基础信息----')
	get_basic_info(soup)
	print('----获取高管信息----')
	get_gg_info(soup)
	print('----获取股东信息----')
	get_gd_info(soup)
	print('----获取对外投资信息----')
	get_tz_info(soup)
