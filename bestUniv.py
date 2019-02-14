# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 10:42:35 2019

@author: 郑永
"""
import re
import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    #从网络上获取网页内容
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""
    

def fillUnivList(ulist,html):
    #提取网页内容中的信息到合适的数据结构
    soup=BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr.find_all('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string])
           

def printUnivList(ulist,num):
    #利用数据结构展示并输出结果
    tplt = "{0:^10}\t{1:{4}^10}\t{2:^10}\t{3:^10}"
    print(tplt.format("排名","学校名称","省份","总分",chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],u[3],chr(12288)))
        
def main():
    uinfo=[]
    url='http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    html=getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,50)
main()