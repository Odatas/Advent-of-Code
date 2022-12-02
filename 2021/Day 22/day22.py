# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 05:59:39 2021

@author: Paddy
"""
import re
with open("day22.txt","r") as f:
    lines = f.read().split('\n')

cubeCoordinates = []
ignore=1000000000
for i in lines:
    cubeInformation=re.findall(r'-?\d+', i)
    cubeInformation = [int(x) for x in cubeInformation]
    
    if cubeInformation[0] < cubeInformation[1]:
        cubeInformation[0] , cubeInformation[1] =cubeInformation[1],cubeInformation[0]
    if cubeInformation[2] < cubeInformation [3]:
        cubeInformation[2] , cubeInformation[3] =cubeInformation[3],cubeInformation[2]
    if cubeInformation[4] < cubeInformation [5]:
        cubeInformation[4] , cubeInformation[5] =cubeInformation[5],cubeInformation[4]
    append=True
    for j in cubeInformation:
        if j > ignore or j < -ignore:
            append=False
            break
    if append:
        cubeInformation.append(i.split(" ")[0])
        cubeCoordinates.append(cubeInformation)
    
cubesOnList={}

for i in cubeCoordinates:
    print(i)
    for x in range(i[1],i[0]+1):
        for y in range(i[3],i[2]+1):
            for z in range(i[5],i[4]+1):
                    newElement = str(x)+" "+str(y)+" "+str(z)
                    if i[6] == "off":
                        try:
                            del cubesOnList[newElement]
                        except:
                            pass
                    else:
                        try:
                            cubesOnList[newElement] =" "
                        except Exception as e:
                            print(e)
print(len(cubesOnList))