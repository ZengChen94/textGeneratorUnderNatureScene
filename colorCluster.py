# -*- coding: cp936 -*-
from pylab import imread,imshow,figure,show,subplot
from numpy import reshape,uint8,flipud
from scipy.cluster.vq import kmeans,vq
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

if __name__ == '__main__':
    img = pathWalk('sceneDataset/')
    length = len(img)
    for i in range(length):
        print i
        imgName = img[i]
        imgName = imgName[0] + '/' +imgName[1]
        textName = imgName[0:len(imgName)-3]+'txt'
        centroids = colorCluster(imgName)
        fileHandle = open ( textName, 'w' )
        for m in centroids:
            k = ' '.join([str(j) for j in m])
            #fileHandle.write(k+"\n")
            fileHandle.write(k+"\n")
        fileHandle.close()


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
