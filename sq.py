import numpy as np 
import cv2
import os
import sys
from termcolor import colored, cprint
import imageio.v3 as iio


def printFrame(image, canvas, startWidth, startHeight):
    lst = [] 
    vctr = np.array(lst) 
    imgRowIndex = 0

    for idx, row in enumerate(canvas):
        for idx2, pixel in enumerate(row):
            ## so print if we have hit the middle point
            ## print if theres still image data on that row
            ## print only if that row has data
            if(idx2 >= startWidth and imgRowIndex < len(image[0]) and idx < len(image)):
                imageBlot = image[idx][imgRowIndex]
                t = colored(".", ( imageBlot[0],  imageBlot[1],  imageBlot[2]),  ( imageBlot[0],  imageBlot[1],  imageBlot[2]))
                lst.append(t)
                imgRowIndex+= 1
            else:
                lst.append(" ")       
        lst.append('\n')
        imgRowIndex = 0


    print(*lst, sep='')

def clearFrame():
    # print(chr(27) + "[2J") could also print the escape chars which is quite cool
    os.system('clear')


def resizeToFit(image_width, image_height, box_width, box_height):
    scale = min(box_width / image_width, box_height / image_height)
    new_width = int(image_width * scale)
    new_height = int(image_height * scale)
    return new_width, new_height

def resizeImage(image):
    imageHeight,imageWidth, _mode = image.shape
    width,height =  os.get_terminal_size()
    nWidth, nHeight = resizeToFit(imageWidth, imageHeight, width, height)
    resized = cv2.resize(image, (nWidth, nHeight));
    return resized

## hm this was interesting i had to use list comprehension
## this is new to me, to python: https://www.geeksforgeeks.org/nested-list-comprehensions-in-python/
## 
def createCanvas():
    width,height = os.get_terminal_size()
    matrix = [[' ' for j in range(width)] for i in range(height)]
    return matrix

def findTheMiddle(image):
    width,height = os.get_terminal_size() ## come back< - i had this as a function bu the value kept changing
    imageHeight,imageWidth, _mode = image.shape
    midScreenWidth = width / 2
    midImageWidth = imageWidth / 2
    midScreenHeight = height / 2
    midImageHeight = imageHeight / 2
    startPrintingAtWidth = round(midScreenWidth -  midImageWidth)
    startPrintingAtHeight = round(midScreenHeight -  midImageHeight)
    start = {
        "width": startPrintingAtWidth,
        "height": startPrintingAtHeight
        }
    return start


def main():
    canvas = createCanvas()
    clearFrame()

    middleWidth = None
    middleHeight = None


    # image = resizeImage(cv2.cvtColor(cv2.imread("./images/earth.gif"), cv2.COLOR_BGR2RGB))

    for idx, frame in enumerate(iio.imiter("<video0>")):

        ## we can't keep up with the framerate of the video so we will skip frames
        if(idx % 60 == 0):
            frame = resizeImage(frame)
            if(middleWidth is None or middleHeight is None):
                middlePoints = findTheMiddle(frame)
                middleWidth = middlePoints["width"]
                middleHeight = middlePoints["height"]
            clearFrame()
            middlePoints = findTheMiddle(frame)
            printFrame(frame, canvas, middleWidth, middleHeight )

       

      

main()