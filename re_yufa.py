#encoding:utf-8
import re


"""
#非正则表达式实现
str1='imooc python'
print str1.find('11') #在字符串中查找'imooc'，－1为字符串不存在'imooc'，反之，输出0
print str1.startswith('imooc') #判断字符串是否以'imooc'开头
print str1.endswith('imooc') #判断字符串是否以'imooc'结尾

print '>>>>>>>>>>>>>>>>>>>'
"""

#正则表达式语法
"""
str1='imooc python'
pa=re.compile(r'imooc') #生成一个判断的对象，也就一个匹配的模式pattern的对象
ma=pa.match(str1) #判断str1是否符合'imooc模式'
print ma.group() #将匹配的字符串地址显示成字符串本身
print ma.span() #返回匹配字符串的索引位置
print ma.string #返回被匹配的字符串
print ma.re #返回pattern实例
"""
"""
str2='imooc python'
pa=re.compile(r'imooc',re.I) #模式忽视大小写
ma=pa.match(str2)
print ma.group()

pa2=re.compile(r'(imooc)',re.I)
ma2=pa2.match(str2)
print ma2.groups() #以元组形式返回匹配的结果

print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
"""

#匹配单个字符
"""
#. 匹配任意字符（除了\n）
#ma=re.match(r'.','b') #.表示匹配任意字符(除了\n)
ma=re.match(r'..','2b') #表示匹配两个字符
print ma.group()

#ma1=re.match(r'{.}','{t}') #匹配大括号中的任意字符
ma1=re.match(r'{..}','{tt}') #表示匹配两大括号中的两个字符
print ma1.group()
"""

"""
#[...] 匹配字符集
ma=re.match(r'{[abc]}','{a}') #匹配字符集中的任意一个字符
print ma.group()
ma1=re.match('[a-zA-Z0-9]','8') #匹配a-zA-Z0-9中任意一个字符,a-zA-Z0-9可以用\w代替
print ma1.group()
"""

"""
#\w ／ \W  匹配单个字符［a-zA-Z0-9］／非单穿字符
ma1=re.match('\w','8') #匹配单个字符［a-zA-Z0-9］
print ma1.group()
ma2=re.match('\W',' ') #匹配非单穿字符
print ma2.group()
"""
"""
#\d ／ \D 匹配数字／非数字
ma=re.match(r'\[[\d]\]','[6]') #匹配任意单个数字
print ma.group()

ma1=re.match(r'\[[\d]\]','[&]') #匹配任意单个数字
print ma1.group()

#\s / \S 匹配空白／非空白字符

print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
"""

#匹配多个字符

"""
# * 匹配前一个字符0次或者无限次
ma=re.match('[A-Z][a-z]*','Abcdef') #匹配一个大写字母＋多个小写字母
print ma.group()

ma1=re.match('[A-Z][a-z]*','A') #匹配一个大写字母＋零个小写字母
print ma1.group()
"""
"""
# + 匹配前一个字符一次或者无限次
ma=re.match('[_a-zA-Z]+[_\w]*','_Abcdef') #匹配python的命名规则：必须是以_字母开头
print ma.group()
"""
"""
# ? 匹配前一个字符0次或者1次
ma=re.match('[1-9]?[0-9]','9') #匹配0-99之间的所有数字
print ma.group()
"""
"""
# {m} / {m,n} 匹配前一个字符m次或者n次
ma=re.match('[a-z0-9]{6}','9a1b3c3') #a-z0-9任意字符出现6次
print ma.group()

ma3=re.match('[A-Za-z0-9]{7}@163.com','9a1b3c3@163.com') #匹配一个163邮箱
print ma3.group()

ma1=re.match('[a-z0-9]{6,9}','9a1b3c4f') #a-z0-9任意字符出现6-9次
print ma1.group()

ma2=re.match('[A-Za-z0-9]{4,9}@163.com','9a1b3c3@163.com') #匹配一个163邮箱
print ma2.group()
"""
"""
# *? / +? / ?? 匹配模式变为非贪婪（尽可能少匹配字符）
ma=re.match('[0-9][a-z]*','6yuio') #a-z匹配任意多个
print ma.group()

ma1=re.match('[0-9][a-z]*?','6yuio') #a-z尽可能少匹配，最好是匹配0个
print ma1.group()

ma2=re.match('[0-9][a-z]+?','6yuio') #a-z尽可能少匹配，最好是匹配1个
print ma2.group()

ma3=re.match('[0-9][a-z]??','6yuio') #a-z尽可能少匹配，最好是匹配0个
print ma3.group()

print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
"""
#边界匹配

"""
# ^ 匹配开头
ma=re.match(r'^[\w]{4,9}@163.com','9a1b3c3@163.comabc') #匹配以[\w]开头的字符串
print ma.group()

"""
"""
# $ 匹配结尾
ma=re.match('[\w]{4,9}@163.com$','9a1b3c3@163.com') #匹配以@163.com结尾的字符串
print ma.group()

ma1=re.match('[\w]{4,9}@163.com$','9a1b3c3@163.comabc') #匹配以@163.com结尾的字符串
print ma1.group()
"""
"""
#\A / \Z 指定的字符串必须出现在开头/结尾
ma=re.match('\Aimooc[\w]*','imoocpython') #匹配以imooc开头的字符串
print ma.group()

ma1=re.match('imooc[\w]*python\Z','imoocpython') #匹配以python结尾的字符串
print ma1.group()

print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
"""

#分组匹配

"""
# | 匹配左右任意一个表达式
ma=re.match('adc|d','adc') #匹配adc或d
print ma.group()

ma1=re.match('[1-9]?\d$|100','100') #匹配0-99或100
print ma1.group()
"""
"""
# (ab) 括号中表达式作为一个分组
ma=re.match(r'[\w]{4,6}@(163|126).com','imooc@163.com') #匹配一个163或126邮箱
print ma
"""
"""
# \<number> 引用编号为num的分组匹配到的字符串 ，经常用在xml中
ma=re.match(r'<([\w]+>)[\w]+</\1','<book>python</book>') #匹配有效的xml
print ma.group()
"""
"""
# (?p<name>) 分组起一个别名
ma=re.match(r'<(?P<mark>[\w]+>)[\w]+</(?P=mark)','<book>python</book>') #匹配有效的xml
print ma.group()

# (?p=name) 引用别名为name的分组匹配字符串
"""

#re模块中其他方法
#match(pattern,string,flags=0) 从字符串开头匹配
#search(pattern,string,flags=0) 在一个字符串中查找匹配
#findall(pattern,string,flags=0) 找到匹配，返回所有匹配部分的列表
#sub(pattern,repl,string,flags=0) 将字符串中匹配正则表达式的部门替换为其他值
#split(pattern,string,maxsplit=0,flags=0) 根据匹配分割字符串，返回分割字符串组成的列

str1='imooc videonum=1000'
"""
print str1.find('1000') #在字符串中查找1000
"""

"""
info=re.search(r'\d+',str1) #在字符串中查找匹配
print info.group()
"""

"""
str2='c++=100,java=90,python=80'
info=re.findall(r'\d+',str2) #在字符串中查找所有匹配的字段
print info
print sum(int(x) for x in info) #求和
"""
"""
str3='imooc videonum=1000'
info=re.sub(r'\d+','1001',str3) #将匹配的字符串替换成1001
print info
"""
"""
str4='imooc videonum=1000'
def add1(match): #定义一个替换的函数
    va1=match.group()
    num=int(va1)+1
    return str(num)
info=re.sub(r'\d+',add1,str4) #传入定义的函数名
print info
"""

str5='imooc:c c++ java python,c#'
info=re.split(r':| |,',str5) #通过':| |,'分割字符串
print info











































































