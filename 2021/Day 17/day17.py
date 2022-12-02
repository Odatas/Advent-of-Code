# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 20:23:44 2021

@author: Paddy
"""

targetxstart = 211
targetxend = 232
targetystart = -124
targetyend = -69

# targetxstart = 20
# targetxend = 30
# targetystart = -10
# targetyend = -5

def runSteps(xvelocity,yvelocity):
    x=0
    y=0
    while True:
        #change position
        x+=xvelocity
        y+=yvelocity
        #change velocity
        yvelocity-=1
        if xvelocity > 0:
            xvelocity-=1
        elif xvelocity < 0:
            xvelocity+=1
        #get highest position
        
        if targetxstart-1 < x < targetxend+1 and targetystart-1 < y < targetyend+1:
            return True
        if x > targetxend or (yvelocity < 0 and y < targetystart):
            return False
        
solutions = []
searchrange= 1000
for y in range(-1000,1000):
    for x in range (-1000,1000):
        if runSteps(x,y):
            print("Nr:",len(solutions),x,y)
            solutions.append((x,y))
print("Part2:",len(solutions))