# -*- coding: cp936 -*-
from pylab import imread,imshow,figure,show,subplot
from numpy import reshape,uint8,flipud
from scipy.cluster.vq import kmeans, kmeans2,vq
import sys
import os.path
import random

def pathWalk(path):
    paths = []
    for root, dirs, files in os.walk( path ):
        for fn in files:
            paths.append([root, fn])
    return paths
 
#img = imread('barca.jpg')
def colorCluster(img):
    img = imread(img)
    
    pixel = reshape(img,(img.shape[0]*img.shape[1],3))
    centroids,_ = kmeans(pixel,3) # six colors will be found
    return centroids

def OsDistance(vector1, vector2):
    distance = (vector1[0]-vector2[0])**2 + (vector1[1]-vector2[1])**2 + (vector1[2]-vector2[2])**2
    return distance

if __name__ == '__main__':
    img = imread('barca.jpg')
    pixel = reshape(img,(img.shape[0]*img.shape[1],3))#reshape
    length = img.shape[0]*img.shape[1]
    centroids,a = kmeans(pixel,3) # three colors will be found
    qnt,_ = vq(pixel,centroids)
    centers_idx = reshape(qnt,(img.shape[0],img.shape[1]))#reshape
    clustered = centroids[centers_idx]
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0
    for i in range(length):
        pixelTmp = pixel[i]
        dist0 = OsDistance(centroids[0], pixelTmp)
        dist1 = OsDistance(centroids[1], pixelTmp)
        dist2 = OsDistance(centroids[2], pixelTmp)
        if min(dist0, dist1, dist2) == dist0:
            cnt0 = cnt0 + 1
        elif min(dist0, dist1, dist2) == dist1:
            cnt1 = cnt1 + 1
        else:
            cnt2 = cnt2 + 1
    #print type(centroids)
    print centroids
    print cnt0, cnt1, cnt2
    if cnt0 > cnt1 > cnt2:
        pass
    elif cnt0 > cnt2 > cnt1:
        centroids[0], centroids[1], centroids[2] = centroids[0], centroids[2], centroids[1]
    elif cnt1 > cnt0 > cnt2:
        centroids[0], centroids[1], centroids[2] = centroids[1], centroids[0], centroids[2]
    elif cnt1 > cnt2 > cnt0:
        centroids[0], centroids[1], centroids[2] = centroids[1], centroids[2], centroids[0]
    elif cnt2 > cnt1 > cnt0:
        centroids[0], centroids[1], centroids[2] = centroids[2], centroids[1], centroids[0]
    elif cnt2 > cnt0 > cnt1:
        centroids[0], centroids[1], centroids[2] = centroids[2], centroids[0], centroids[1]
    print centroids
    #figure(1)
    #subplot(221)
    #imshow(img)
    #subplot(224)
    #imshow(clustered)
    #subplot(223)
    #imshow(centers_idx)
    #show()


'''
    result = []
    fileHandle = open ( textName, 'r' )
    for line in fileHandle.readlines():
        line = line[0:-1]
        #resultInLine = map(int, line.split(' '))
        result.append(map(int, line.split(' ')))
        #result.append(list(map(int,line.split(','))))    
    fileHandle.close()

    print centroids
    print result
    '''

    
#print centroids
#a = centroids[0]
#print a
#b = a[0]
#print b
#print b+2

# quantization 聚类
#qnt,_ = vq(pixel,centroids)
 
# reshaping the result of the quantization
#centers_idx = reshape(qnt,(img.shape[0],img.shape[1]))
#centroids：质心
#clustered = centroids[centers_idx]
 
#figure(1)
#subplot(211)
#imshow(img)
#subplot(212)
#imshow(clustered)
#show()
