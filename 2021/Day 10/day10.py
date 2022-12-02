# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 07:05:05 2021

@author: pphilipiak
"""

with open("day10.txt","r") as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]
clampPairs = {
    "(":")",
    "[":"]",
    "{":"}",
    "<":">",

    }
clampScore = {
    ")":3,
    "]":57,
    "}":1197,
    ">":25137
    }

clampScoreAutoComplete = {
    ")":1,
    "]":2,
    "}":3,
    ">":4
    }


score=0
incompleteScores=[]
for i in lines:
    closeClamps=[]
    discard = False
    for j in i:
        try:
            closeClamps.append(clampPairs[j])
        except KeyError:

            if j == closeClamps[len(closeClamps)-1]:
                closeClamps = closeClamps[:-1]
            else:
                score += clampScore[j]
                discard = True
                break
    if(len(closeClamps) > 0) and not discard:
        tempScore=0
        for k in reversed(closeClamps):
            tempScore *=5
            tempScore +=clampScoreAutoComplete[k]
        incompleteScores.append(tempScore)
print("Part 1:",score)
incompleteScores.sort()
print("Part2:",incompleteScores[int(len(incompleteScores)/2)])
