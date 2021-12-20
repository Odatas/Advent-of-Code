# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 21:13:35 2021

@author: Paddy
"""
#applys the enchance algorythm
def enchance(img):
    newImage=[]
    h = len(img)
    w = len(img[0])
    for iy in range(1,h-1):
        lineString=[]
        for ix in range(1,w-1):
            binaryString=""
            for step in steps:
                if 0 <= iy+step[0] < h and 0 <=ix+step[1] < w:
                    binaryString+=conversion[img[iy+step[0]][ix+step[1]]]
                else:
                    binaryString += "0"
            lineString.append(imgEnhcAlgo[int(binaryString,2)])
        newImage.append(lineString)
    return newImage

#counts the #
def countHastags(img):
    counter = 0
    for i in img:
        for j in i:
            if j == "#":
                counter+=1
    return counter

#adds a padding to the image 3* the size of the image. 
def extendImg(img):
    w = len(img)
    biggerImgMatrix = []
    for i in range(w):
        string=[]
        for j in range(3*w):
            string.append(".")
        biggerImgMatrix.append(string)
    for i in range(w):
        string=[]
        for j in range(w):
            string.append(".")
        string+=imgMatrix[i]
        #print(i,string)
        for j in range (w):
            string.append(".")
        biggerImgMatrix.append(string)
    for i in range(w):
        string=[]
        for j in range(3*w):
            string.append(".")
        biggerImgMatrix.append(string)
    return biggerImgMatrix
    

with open("day20.txt","r") as f:
    lines = f.read().split('\n')
imgEnhcAlgo=lines.pop(0)

lines=lines[1:]
w,h = len(lines[0]), len(lines)
imgMatrix = [[list(lines[y])[x] for x in range(w)] for y in range(h)]
imgMatrix = extendImg(imgMatrix)
conversion = {
    ".":"0",
    "#":"1"
    }

steps=[]
for i in range(-1,2):
    for j in range(-1,2):
        steps.append((i,j))
for i in range(50):
    imgMatrix = enchance(imgMatrix)
    if i == 1:
        print("Part1:",countHastags(imgMatrix))
print("Part2:",countHastags(imgMatrix))


