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
    #9,6 and 0 all have 6 bits.
    sixerList = [x for x in entry if len(x) == 6]
    for i in sixerList:
        if containsAll(i,wireDict[4]):
            #between 9,6 and zero, 9 is the only one that contains all bits of 4
            wireDict[9]=i
    sixerList.remove(wireDict[9])
    for i in sixerList:
        if containsAll(i,wireDict[1]):
            #between 6 and 0, 0 contains all bits from 1
            wireDict[0] = i
    sixerList.remove(wireDict[0])
    #6 is whats left in the list
    wireDict[6] = sixerList[0]
    #3,5 and 2 all have 5 bits
    fiverList = [x for x in entry if len(x) == 5]
    for i in fiverList:
        if containsAll(i,wireDict[1]):
            #between 3,5 and 2  3 is the only one that dcontains all bits from 1
            wireDict[3] = i
            break
    fiverList.remove(wireDict[3])
    #get the one bit that is in 1 but not in 6
    lastQlue = [x for x in wireDict[1] if x in wireDict[6]][0]
    for i in fiverList:
        if lastQlue in i:
            #5 has the one bit that is in 1 but not in 6
            wireDict[5] = i
    fiverList.remove(wireDict[5])
    #2 is whats left.
    wireDict[2] = fiverList[0]

    return wireDict



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



