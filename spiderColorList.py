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
    reg = r'<td align="right">(.+?)</td>'#������ʽ���ַ���
    imgre = re.compile(reg)#reģ���ṩ��������ʽ��֧��,����ΪPatternʵ��
    imglist = imgre.findall(html)
    print imglist

