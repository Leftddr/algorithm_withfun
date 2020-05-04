import glob, os
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import time

url = "http://iphak.ssu.ac.kr/2014/guide/notice.asp"
page_set = []

html = urlopen(url)
bsObj = BeautifulSoup(html, "html.parser")
for i in range(5):
    global page_set
    for link in bsObj.findAll("a", href = re.compile("notice_view.asp*")):
        if 'href' in link.attrs:
            print(link.get_text())
    page = bsObj.find("a", href = re.compile("^(\?page=*)"))
    if page['href'] in page_set:
        while(True):
            page = bsObj.find("a", href = re.compile("^(\?page=*)"))
            if page['href'] not in page_set:
                page_set.append(page['href'])
    final_url = url + page['href']
    print(final_url)
    time.sleep(3)
    html = urlopen(final_url)
    bsObj = BeautifulSoup(html, "html.parser")

    
        

'''
flist = glob.glob('/home/kernel/Desktop/*')
for fname in flist:
    if os.path.isfile(fname):
        print(fname + ' [FILE]')
    elif os.path.isdir(fname):
        print(fname + ' [DIR]')
    elif os.path.islink(fname):
        print(fname + ' [SYMBOLIC LINK]')
'''
    