# coding:utf-8

from urllib import request
import http.cookiejar

url = "http://www.aisixiang.com/thinktank/yangguangbin.html"
# url = "http://www.baidu.com"
"""
print('第一种方法')
response1 = request.urlopen(url)
print(response1.getcode())
print(len(response1.read()))
"""

print('第二种方法')

request1 = request.Request(url)
request1.add_header("user-agent", "Mozilla/5.0")
response2 = request.urlopen(request1)
print(response2.getcode())
print(len(response2.read()))

print('第三种方法')

# 设置cookie
cj = http.cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cj))
request.install_opener(opener)
response3 = request.urlopen(url)
print(response3.getcode())
print(cj)
# website's content
print(response3.read())
