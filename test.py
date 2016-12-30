import re
from urllib import parse
from urllib import request
from bs4 import BeautifulSoup

# 使用get方法发送请求
reqGet = request.Request("http://www.baidu.com")
reqGet.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36")
respGet = request.urlopen(reqGet)
#print(respGet.read().decode("utf-8"))





# 使用post方法发送请求
reqPost = request.Request("http://www.dev4free.com/devbuy_web/java/manageplatform/login.action")
postData = parse.urlencode([("name","test"),("password","test")])
reqPost.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36")
respPost = request.urlopen(reqPost,data=postData.encode("utf-8"))
# print(respPost.read().decode("utf-8"))





#解析http://www.dev4free.com首页所有的图片地址
responese = request.urlopen("http://www.dev4free.com").read().decode("utf-8")
soup = BeautifulSoup(responese,"html.parser")
images = soup.findAll("img", src=re.compile("^(images)"))
for imagesUrl in images:
   print("http://www.dev4free.com/" + imagesUrl["src"])