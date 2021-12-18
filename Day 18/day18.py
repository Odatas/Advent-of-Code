# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 15:58:26 2021

@author: Paddy
"""

import json
import math




def exploderHelper(Term,number):
    if isinstance(Term, list):
        if exploderHelper(Term[0], number):
            Term[0]+=number
        return False
    else:
        return True
    
def exploderHelperFromBehinde(Term,number):
    if isinstance(Term, list):
        if exploderHelperFromBehinde(Term[len(Term)-1], number):
            Term[len(Term)-1]+=number
        return False
    else:
        return True

def explode(Term,level):
    exploder = [0,0]
    #0 counts so >3 is actually 5 levels
    if level > 3 and isinstance(Term, list):
        global therewasanexplosion
        therewasanexplosion = True
        return True, None
    if isinstance(Term,list) and not therewasanexplosion:
        for i in  range(len(Term)):
            if not therewasanexplosion:
                exploded, exploder = explode(Term[i],level+1)
            if exploded:
                exploder = Term[i]
            if exploder[0] != 0 and i > 0:
                try:
                    if isinstance(Term[i-1], list):
                        exploderHelperFromBehinde(Term[i-1],exploder[0])
                    else:
                        Term[i-1]+=exploder[0]
                    exploder[0] = 0
                except Exception as e:
                    print(e)
                    pass
            if exploder[1] != 0:
                try:
                    if isinstance(Term[i+1], list):
                        exploderHelper(Term[i+1],exploder[1])
                    else:
                        Term[i+1]+=exploder[1]
                    exploder[1] = 0
                except Exception as e:
                    #print(e)
                    pass
            
            if exploded:
                Term[i] = 0
                #print("Changed this",Term)
                break
            if therewasanexplosion:
                break
    #print("exploder",exploder)
    return False, exploder

def splitting(Term):
    if isinstance(Term,list):
        for i in range(len(Term)):
            if isinstance(Term[i],list):
                seperated = splitting(Term[i])
                if seperated == True:
                    return True
            else:
                if Term[i] > 9:
                    Term[i] = [math.floor(Term[i]/2),math.ceil(Term[i]/2)]
                    return True
    else:
        print("Bad")
        

def calculateMagnitude(Term):
    
    if len(Term) == 2:
        if isinstance(Term[0], list):
            A=calculateMagnitude(Term[0])
        else:
            A=Term[0]
        if isinstance(Term[1], list):
            B=calculateMagnitude(Term[1])
        else:
            B=Term[1]
        return 3*A+2*B
    else:
        summenHalter=[]
        for i in Term:
            if isinstance(i, list()):
                summenHalter.append(calculateMagnitude(i))
            else:
                summenHalter.append(i)
        return sum(summenHalter)
    


with open("day18.txt","r") as f:
    lines = f.read().split('\n')

mathTerm=[]
therewasanexplosion = False
for i in lines:
    if mathTerm==[]:
        mathTerm = list(eval(i))
    else:
        mathTerm = [mathTerm,list(eval(i))]
    while True:
        explode(mathTerm,0)
        if therewasanexplosion:
            therewasanexplosion = False
            #print("after explode:",mathTerm)
            continue
        split = splitting(mathTerm)
        if split:
            #print("after split:  ",mathTerm)
            continue
        break
    #print("Result:       ",mathTerm)
print("Part1:",calculateMagnitude(mathTerm))
highestNumber=0
for i in range(len(lines)-1):
    for j in range(len(lines)-1):
        if lines[i] == lines[j]:
            continue
        mathTerm = [list(eval(lines[i])),list(eval(lines[j]))]
        while True:
            explode(mathTerm,0)
            if therewasanexplosion:
                therewasanexplosion = False
                #print("after explode:",mathTerm)
                continue
            split = splitting(mathTerm)
            if split:
                #print("after split:  ",mathTerm)
                continue
            break
        magnitude = calculateMagnitude(mathTerm)
        if  magnitude > highestNumber:
            highestNumber = magnitude
        mathTerm = [list(eval(lines[j])),list(eval(lines[i]))]
        while True:
            explode(mathTerm,0)
            if therewasanexplosion:
                therewasanexplosion = False
                #print("after explode:",mathTerm)
                continue
            split = splitting(mathTerm)
            if split:
                #print("after split:  ",mathTerm)
                continue
            break
        magnitude = calculateMagnitude(mathTerm)
        if  magnitude > highestNumber:
            highestNumber = magnitude
print(highestNumber)

