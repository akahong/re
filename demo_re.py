#encoding:utf-8
import urllib2
import urllib
import re

req=urllib2.urlopen('http://www.imooc.com/course/list') #打开慕课网的网页
buf=req.read() #将请求返回的数据存入缓冲区
#print buf

listurl=re.findall(r'http:.+\.jpg',buf)
for url in listurl:
    print url

"""
i=0
for url in listurl:
    with open(str(i)+'.jpg','w') as f:
        req=urllib2.urlopen(url)
        buf=req.read()
        f.write(buf)
        i+=1
"""
