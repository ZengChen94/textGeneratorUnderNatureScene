#!/usr/bin/env python
# http://fengmm521.blog.163.com/blog/static/25091358201512013147207/
#convert -size 320x100 xc:transparent -font arial -pointsize 72 -fill black   -annotate +24+64 Anthony  trans_stamp.png
import Image  
import sys

def cropText(name):
    im = Image.open(name)
    width = im.size[0]  
    height = im.size[1] 
    #print "/* width:%d */"%(width)  
    #print "/* height:%d */"%(height) 
    alpha = im.convert('RGBA').split()[-1]
     
     
    left = width-1
    right = 0
    high = height - 1
    low = 0

    for h in range(0, height):  
        for w in range(0, width):  
            if alpha.getpixel((w, h)) != 0:
                if h < high: high = h
                if h > low: low = h
                if w < left: left = w
                if w > right: right = w

    width = right - left + 1
    height = low - high + 1
    return left, right, high, low, width, height
    #print left, right, high, low
    #print width, height
    #convert trans_stamp.png -crop widthxheight+left+high new.png

#name = 'trans_stamp.png'
#[left, right, high, low, width, height] = cropText(name)
#print left, right, high, low, width, height
