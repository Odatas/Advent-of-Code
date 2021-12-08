# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 12:37:30 2021

@author: Spongetheone
"""


def containsAll(str, set):
    """ Check whether sequence str contains ALL of the items in set. """
    return 0 not in [c in str for c in set]

def createDict(entry):
    wireDict={

    0: "",
    1: "",
    2: "",
    3: "",
    4: "",
    5: "",
    6: "",
    7: "",
    8: "",
    9: "",

    }
    #1
    wireDict[1] = [x for x in entry if len(x) == 2 ][0]
    #7
    wireDict[7] = [x for x in entry if len(x) == 3 ][0]
    #4
    wireDict[4] = [x for x in entry if len(x) == 4 ][0]
    #8
    wireDict[8] = [x for x in entry if len(x) == 7 ][0]
    sixerList = [x for x in entry if len(x) == 6]
    for i in sixerList:
        if containsAll(i,wireDict[4]):
            #9
            wireDict[9]=i
    sixerList.remove(wireDict[9])
    for i in sixerList:
        if containsAll(i,wireDict[1]):
            #0
            wireDict[0] = i
    sixerList.remove(wireDict[0])
    #6
    wireDict[6] = sixerList[0]
    fiverList = [x for x in entry if len(x) == 5]
    for i in fiverList:
        if containsAll(i,wireDict[1]):
            #3
            wireDict[3] = i
            break
    fiverList.remove(wireDict[3])
    lastQlue = [x for x in wireDict[1] if x in wireDict[6]][0]
    for i in fiverList:
        if lastQlue in i:
            wireDict[5] = i
    fiverList.remove(wireDict[5])
    wireDict[2] = fiverList[0]

    return wireDict
    #return  {v: k for k, v in wireDict.items()}



with open("day8.txt") as f:
    lines = f.readlines()

countUnique = 0
totalCount = 0

for i in lines:

    wireDict = createDict(i.split(" | ")[0].split(" "))
    print("\n\nLine: ",i,"\n")
    print(wireDict)
    number=""
    for j in i.split(" | ")[1].split(" "):

        if len(j.strip()) == 2 or len(j.strip()) == 3 or len(j.strip()) == 4 or len(j.strip()) == 7:
            countUnique +=1
        print("Entry is: ",j)
        for i in wireDict:
            if len(wireDict[i]) == len(j.strip()) and containsAll(wireDict[i],j.strip()):

                print("Number is:",i)
                number += str(i)
    print("Number",number)
    totalCount +=int(number)


print("\n\n\n")
print ("Part 1:", countUnique)
print("Part 2:",totalCount)



