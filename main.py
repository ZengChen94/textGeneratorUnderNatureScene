# -*- coding: cp936 -*-
import os
import sys
import os.path
import random
import math

def pathWalk(path):
    paths = []
    for root, dirs, files in os.walk( path ):
        for fn in files:
            paths.append([root, fn])
    return paths

if __name__ == '__main__':
    
    fonts = pathWalk('fonts/')
    randomFont = random.choice(fonts)
    randomFont = randomFont[0] + randomFont[1]

    words = raw_input("input words, please:")
    saveName = './dataset/' + words + '.png'
    print words
    length = len(words)#blank is included
    pointsize = 72
    wordsHeight = pointsize
    wordsWidth = int(pointsize * 5/7) * length
    #whether slant, yes or no both with probility 50%
    if random.randint(1, 2) == 1:
        rotateX = random.randint(1, 10);
    else:
        rotateX = random.randint(350, 360);
    #whether italic, yes or no both with probility 50%
    if random.randint(1, 2) == 1:
        rotateY = rotateX + random.randint(15, 25)
    else:
        rotateY = rotateX
        '''#adjust the size of bg and position of text
    alpha = math.pi * 2 - math.pi / 180 * rotateX
    wordsHeightRotate = wordsHeight * math.sin(alpha) + wordsWidth * math.cos(alpha)
    wordsWidthRotate = wordsHeight * math.cos(alpha) + wordsWidth * math.sin(alpha)
    print wordsWidth, wordsHeight
    print wordsWidthRotate, wordsHeightRotate
    '''
    sizeHeight = wordsHeight + 30*2;
    sizeWidth = wordsWidth + 30*2;
    offsetX = random.randint(25, 35);
    offsetY = random.randint(25, 35) + pointsize;
    sizeWeightHeight = str(sizeWidth) + 'x' + str(sizeHeight)
    sizeAnnotote = str(rotateX) + 'x' + str(rotateY) + '+' + str(offsetX) + '+' + str(offsetY)
    shadowAnnotote = str(rotateX) + 'x' + str(rotateY) + '+' + str(offsetX+5) + '+' + str(offsetY+5)
#windows_path = 'C:\Users\itsy\Desktop'
#os.chdir(windows_path)
#command = 'convert -size 320x100 xc:lightblue  -font Candice -pointsize 72 -tile bg.gif  -undercolor dodgerblue  -stroke navy  -strokewidth 2 -gravity center  -draw "text 0,0' + 'Anthony'+'" text_options.gif'
#command = 'convert -size 320x100 xc:lightblue -font ' + randomFont + ' -pointsize ' + str(pointsize) + ' -annotate 350x350+20+90 ' + words + ' ' + saveName

    command = 'convert -size ' + sizeWeightHeight + ' xc:lightblue' + ' -font ' + randomFont + ' -pointsize ' + str(pointsize)
    #whether shadow, yes or no both with probility 50%
    if random.randint(1, 2) == 1:
        command = command + ' -annotate ' + shadowAnnotote + ' ' + words + ' -blur 0x4 '
    #pure or gradient color, yes or no both with probility 50%
    if random.randint(1, 2) == 1:
        command = command + ' -fill blue '
    else:
        command = command + ' -tile gradient:blue-red '
    #single stroke, double stroke or none, yes or no both with probility 50%
    tmp = random.randint(1, 3)
    if tmp == 1:
        command = command + ' -stroke navy -strokewidth 2 '
        command = command + ' -annotate ' + sizeAnnotote + ' ' + words + ' '
    elif tmp == 2:
        command = command + ' -stroke black -strokewidth 3 '
        command = command + ' -annotate ' + sizeAnnotote + ' ' + words + ' '
        command = command + ' -stroke white -strokewidth 1 '
        command = command + ' -annotate ' + sizeAnnotote + ' ' + words + ' '
    else:
        command = command + ' -annotate ' + sizeAnnotote + ' ' + words + ' '
    #whether blur, yes or no both with probility 50%
    if random.randint(1, 2) == 1:
        command = command + ' -blur 0x3 '

    #make the whole font look like it is a 3 dimensional mountain ridge
    #command = command + ' -shade 135x30 -auto-level +level 10,90% '

    #mooth the result to generate a better and strangely shiny look to the resulting font
    #command = command + ' -adaptive-blur 0x2 '

    #wave
    #command = command + ' -wave -50x640 -crop x110+0+10 '
    command = command + saveName
    os.system(command)
