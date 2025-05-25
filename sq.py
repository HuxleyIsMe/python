from matplotlib.image import imread

import numpy as np 
import cv2
import os
import sys
from termcolor import colored, cprint

def printFrame(image):
    lst = [] 
    vctr = np.array(lst) 
    for row in image:
        for pixel in row:
            t = colored(".", ( pixel[0],  pixel[1],  pixel[2]),  ( pixel[0],  pixel[1],  pixel[2]))
            lst.append(t)
        lst.append('\n')
    print(*lst, sep='')

def clearFrame():
    # print(chr(27) + "[2J") could also print the escape chars which is quite cool
    os.system('clear')


def userScreenDimensions():
    width, height = os.get_terminal_size()
    return {width, height}


def resizeToFit(image_width, image_height, box_width, box_height):
    scale = min(box_width / image_width, box_height / image_height)
    new_width = int(image_width * scale)
    new_height = int(image_height * scale)
    return new_width, new_height

def resizeImage(image):
    imageHeight,imageWidth, _mode = image.shape
    width, height = userScreenDimensions()
    nWidth, nHeight = resizeToFit(imageWidth, imageHeight, width, height)
    resized = cv2.resize(image, (nWidth, nHeight));
    return resized




### need to get users terminal size 

userScreenDimensions()
resizedImage = resizeImage(imread("./sq.jpg"))
clearFrame()
printFrame(resizedImage)

### need to get image size

### work out image ratio

### get smaller value from users terminal size 

### rescale image to fit in the terminal