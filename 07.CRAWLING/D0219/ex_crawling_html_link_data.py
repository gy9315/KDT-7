from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import urllib.error as error  
pages_set=set()
count=0
def get_links(page_url):
    global pages_set
    global count
    html=urlopen(f'https://en.wikipedia.org/{page_url}')
    soup=BeautifulSoup(html,'html.parser')
    # -----------------------------------------------------------------
    # 정보수집
    try:
        print(soup.h1.text)
        print(soup.select_one('attrs#mw-content-text').select_one('p').text)
    except AttributeError as e:
        print('this page is missing something! continuing:',e)
    # -----------------------------------------------------------------
    for link in soup.find_all('a',href=re.compile('^(/wiki/)((?!:).)*$')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages_set:
                new_page=link.attrs['href']
                count+=1
                print(f'[{count}]: {new_page}')
                pages_set.add(new_page)
                get_links(new_page)
                
                
get_links('')