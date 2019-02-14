# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 19:22:17 2019

@author: Administrator
"""

import re
import requests
def getHTMLText(url):
    #提交商品搜索请求，循环获取页面
    try:
      kv={'user-agent':'Mozilla/5.0'}  
      r=requests.get(url,headers=kv)
      r.raise_for_status()
      r.encoding=r.apparent_encoding
      print(r.request.headers)
      return r.text
    except:
        print("获取页面失败")
        return ""

    
    
def parsePage(ilt,html):
    #对于每一个页面，提交商品名称和价格信息到合适的数据结构
    try:
        plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt=re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price=eval(plt[i].split(':')[1])
            title=eval(tlt[i].split(':')[1])
            ilt.append([price,title])
            
    except:
            print("提取信息到数据结构失败")

    
def printGoodsList(ilt):
    #将信息输出到屏幕
    tplt="{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count=0
    for g in ilt:
        count=count+1
        print(tplt.format(count,g[0],g[1]))
    print("输出到屏幕失败")
    
def main():
    goods='手机'
    depth=2
    start_url='https://s.taobao.com/search?q='+goods
    infoList=[]
    for i in range(depth):
        try:
            url=start_url+'&s='+str(44*i)
            html=getHTMLText(url)
            #print(html)
            parsePage(infoList,html)
        except:
            continue
    printGoodsList(infoList)
    
main()
            
            