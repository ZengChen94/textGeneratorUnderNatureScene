# -*- coding: cp936 -*-
import re
import bs4
import requests
import urllib
import urllib2

def getHtml(url):
    page = urllib2.urlopen(url)
    html = page.read()
    return html

if __name__ == '__main__':
    html = getHtml('http://www.imagemagick.org/script/color.php')
    reg = r'<td align="right">(.+?)</td>'#正则表达式的字符串
    imgre = re.compile(reg)#re模块提供对正则表达式的支持,编译为Pattern实例
    imglist = imgre.findall(html)
    print imglist

