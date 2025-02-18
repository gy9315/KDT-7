from urllib.request import Request
from urllib.request import urlopen
from bs4 import BeautifulSoup
url='https://www.melon.com/chart/index.htm'
urlrequest=Request(url,headers={'user-agent':'mozilla/5.0'})
html=urlopen(urlrequest)
bs=BeautifulSoup(html,'html.parser')
print(bs)
