#!/usr/bin/env python
# coding=utf-8

import urllib
import urllib2
import sys

# 通过wireshark抓包获取,发现有异常,无法成功
#url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

# 通过fiddler获取的
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

# 完整的headers
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Content-Type": " application/x-www-form-urlencoded; charset=UTF-8",
}


def show_usage():
    print "Input a keyword"


if len(sys.argv) <= 1:
    show_usage()
    sys.exit(1)

# 用户输入需要翻译的词
#key = raw_input("Enter the word need to translate : ")
key = sys.argv[1]

# 需要发送到web服务器的表单数据
formdata = {
    "i": key,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTIME",
    "typoResult": "false"
}

# 经过urlencode编码
data = urllib.urlencode(formdata)

# 如果Request方法传入data参数的话就表示这个请求是POST
# 如果没有就表示是GET请求
request = urllib2.Request(url, data=data, headers=headers)

conn = urllib2.urlopen(request)
html = conn.read()

# simplely parse the result in rudely way, not that smart
print html[html.find("tgt") + 6:-6]
