from urllib import request
import http.cookiejar

url = 'http://www.baidu.com'

print('-'*30)
print('第一种方法')

resp1 = request.urlopen(url)
print(resp1.getcode())
print(len(resp1.read()))

print('-'*30)
print('第二种方法')

req = request.Request(url)
req.add_header('user-agent','Mozilla/5.0')
#伪装成其他的浏览器
resp2 = request.urlopen(req)

print(resp2.getcode())
print(len(resp2.read()))

print('-'*30)
print('第三种方法')

cj = http.cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cj))
request.install_opener(opener)
#urllib有了cookie数据增强的水平

resp3 = request.urlopen(url)

print(resp3.getcode())
print(cj)
print(len(resp3.read()))

