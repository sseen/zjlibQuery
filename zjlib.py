import requests
from bs4 import BeautifulSoup

zlibUrlLogin = 'http://opac.zjlib.cn/opac/reader/login'
zlibUrlDoLogin = 'http://opac.zjlib.cn/opac/reader/doLogin'

user = {'rdid':'id','rdName':'name','returnUrl':'','password':''}

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:57.0) Gecko/20100101 Firefox/57.0',
           'Host':'opac.zjlib.cn',
           'Referer':'http://opac.zjlib.cn/opac/reader/login'}

conn = requests.session()

r = conn.post(zlibUrlDoLogin, headers=headers, data=user)

# read info
mypageHtml = r.text
soup=BeautifulSoup(mypageHtml,'lxml')
allTds = soup.select('#contentTable > tr > td')
for td in allTds:
    print(td.get_text())
