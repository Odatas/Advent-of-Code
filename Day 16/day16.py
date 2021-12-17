# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 08:27:04 2021

@author: Paddy
"""

versionSum = 0
tree=""
bytePointer = 0



with open("day16.txt","r") as f:
    lines = f.readlines()

#hexadecimal = lines[0].strip()
hexadecimal = "8A004A801A8002F478"
end_length = len(hexadecimal) * 4
hex_as_int = int(hexadecimal, 16)
hex_as_binary = bin(hex_as_int)
padded_binary_original = hex_as_binary[2:].zfill(end_length)
padded_binary_original_size = len(padded_binary_original)

def applyId(listOfNumbers,ID):
    print(tree+"ApplyID:",listOfNumbers,ID)
    if ID == 0:
        return sum(listOfNumbers)
    if ID ==1:
        result = 1
        for x in listOfNumbers:
            result = result *x
        return result
    if ID == 2:
        return min(listOfNumbers)
    if ID == 3:
        return max(listOfNumbers)
    if ID == 5:
        if listOfNumbers[0] > listOfNumbers[1]:
            return 1
        else:
            return 0
    if ID ==6:
        if listOfNumbers[0] < listOfNumbers[1]:
            return 1
        else:
            return 0
    if ID ==7:
        if listOfNumbers[0] == listOfNumbers[1]:
            return 1
        else:
            return 0
    print("Shit")
        
        


def bytesToNumber(subpackages=-1,lengthlimit = -1):
    
    global bytePointer
    global tree
    numbersArray=[]
    test = []
    tree += "|"
    while bytePointer+6 < padded_binary_original_size and subpackages != 0 and lengthlimit !=0 :
        #print(tree+"Parsed",padded_binary_original[bytePointer:])
        version = int(padded_binary_original[bytePointer:bytePointer+3],2)
        bytePointer+=3
        lengthlimit-=3
        typeID = int(padded_binary_original[bytePointer:bytePointer+3],2)
        bytePointer +=3
        lengthlimit-=3
        print(tree)
        #print(tree+"Version:",version,"Type ID:",typeID,)
        global versionSum
        versionSum += version
        #literal value
        if typeID == 4:
            stringliteral=""
            while True:
                stringliteral += padded_binary_original[bytePointer+1:bytePointer+5]
                bytePointer +=5
                lengthlimit-=5
                if padded_binary_original[bytePointer-5]=="0":
                    subpackages-=1
                    break
            numbersArray.append(int(stringliteral,2))
            print(tree+"Literal Value:",int(stringliteral,2))
            if subpackages == 0 or lengthlimit == 0:
                tree = tree[1:]
                return numbersArray
        else:
            typeLength = padded_binary_original[bytePointer]
            bytePointer+=1
            lengthlimit-=1
            if typeLength == "0":
                breaker = 15
                number = int(padded_binary_original[bytePointer:bytePointer+breaker],2)
                bytePointer += breaker
                lengthlimit -= breaker
                #print(tree+"intlenght",number)
                numbersArray = bytesToNumber(lengthlimit=number)
                #print(tree+"Back from length",numbersArray)
                subpackages-=1
                test.append(applyId(numbersArray, typeID))
                #print(tree+str(test))
                #return test
            else:
                breaker=11
                number = int(padded_binary_original[bytePointer:bytePointer+breaker],2)
                bytePointer +=breaker
                lengthlimit -= breaker
                #print(tree+"packagelength",number)
                numbersArray = bytesToNumber(subpackages=number)
               # print(tree+"Back from package",numbersArray)
                subpackages-=1
                test.append(applyId(numbersArray, typeID))
                #print(tree+str(test))
                #test
    tree = tree[1:]
    print(tree)
    if len(test) > 0:
        return test
    else:
        return numbersArray
part2=bytesToNumber(-1)
print("-------------------------------------\n\nPart:1",versionSum)
print("Part2:",part2)

