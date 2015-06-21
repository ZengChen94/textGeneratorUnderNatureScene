# -*- coding: cp936 -*-
import re
import bs4
import requests
import urllib
import urllib2
import os
import time
def getHtml(url):
    page = urllib2.urlopen(url)
    html = page.read()
    return html

def getFontList(html):
    reg = r'href="(fonts.+?)" title'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    return imglist
    
def getFonts(html):
    reg = r'href="(http://fonts.cncdn.cn.+?)" title'
    imgre = re.compile(reg)
    fontlist = imgre.findall(html)
    return fontlist


if __name__ == '__main__':
    mainHtml = getHtml("http://www.googlefonts.cn/")
    imglist = getFontList(mainHtml)
    for i in imglist:
        reg = r'font=(.+)'
        namere = re.compile(reg)
        name = namere.findall(i)
        name = name[0]
        href = "http://www.googlefonts.cn/" + i
        html = getHtml(href)
        fontlist = getFonts(html)
        cnt = 1
        for j in fontlist:
            print j
            tmp = 1
            while(tmp == 1):
                try:
                    urllib.urlretrieve(j, filename='googleFonts/'+name+str(cnt)+'.ttf', reporthook=None, data=None)
                    tmp = 0
                except:
                    pass
            cnt = cnt + 1
