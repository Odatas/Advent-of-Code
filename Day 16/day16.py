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
hexadecimal = "9C0141080250320F1802104A08"
end_length = len(hexadecimal) * 4
hex_as_int = int(hexadecimal, 16)
hex_as_binary = bin(hex_as_int)
padded_binary_original = hex_as_binary[2:].zfill(end_length)
padded_binary_original_size = len(padded_binary_original)

#function to give number and id to to perform the operation.
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
    #bytepointer is the current position in byte string.
    global bytePointer
    #tree is just for visualisation
    global tree
    #numberarray for numbers and test is array for calculated numbers
    numbersArray=[]
    test = []
    tree += "|"
    #loop that runs through every step as long as there is enough space for headder
    #other counditions are all packages (typeLength=1) found and length of number is reached (typeLength=0)
    #subpackages is for typeLength = 1 and lengthlimit for typelength = 0
    while bytePointer+10 < padded_binary_original_size and subpackages != 0 and lengthlimit !=0 :
        
        #print(tree+"Parsed",padded_binary_original[bytePointer:])
        #print(tree+"lenghtlimit:",lengthlimit,"subpackages:",subpackages)
        version = int(padded_binary_original[bytePointer:bytePointer+3],2)
        bytePointer+=3
        lengthlimit-=3
        typeID = int(padded_binary_original[bytePointer:bytePointer+3],2)
        bytePointer +=3
        lengthlimit-=3
        #print(tree)
        #print(tree+"Version:",version,"Type ID:",typeID,)
        #variable for part 1
        global versionSum
        versionSum += version
        #literal value
        #typeID is 4 then its a literal value
        if typeID == 4:
            stringliteral=""
            #loops as long as a there is a 1 on the first bit of 5 bit part
            while True:
                #save only the 4 last bits of the 5 bit package
                stringliteral += padded_binary_original[bytePointer+1:bytePointer+5]
                bytePointer +=5
                lengthlimit-=5
                #if the first bit is 0 break loop
                if padded_binary_original[bytePointer-5]=="0":
                    subpackages-=1
                    break
            #add that number to the numbers array
            numbersArray.append(int(stringliteral,2))
            print(tree+"Literal Value:",int(stringliteral,2))
            if subpackages == 0 or lengthlimit == 0:
                #if one of the conditions for typeLength is met go back.
                tree = tree[1:]
                print(tree)
                return numbersArray
        else:
            print(tree+"Operator: " + str(typeID))
            #if typeID is not 4 get typeLength
            typeLength = padded_binary_original[bytePointer]
            bytePointer+=1
            lengthlimit-=1
            #if typelegnth is 0
            if typeLength == "0":
                breaker = 15
                #get the 15 bit number and parse it as lengthlimit to the function again recursion goes brr
                number = int(padded_binary_original[bytePointer:bytePointer+breaker],2)
                bytePointer += breaker
                lengthlimit -= breaker
                
                #print(tree+"intlenght",number)
                tempPointer = bytePointer
                test = bytesToNumber(subpackages=subpackages,lengthlimit=number)
                lengthlimit -= (bytePointer-tempPointer)
                lengthlimit-=number
                #print(tree+"lenghtlimit0",lengthlimit)
                #print(tree+"Back from length",numbersArray)
                subpackages-=1
                #apply operation to numbers that got back
                numbersArray.append(applyId(test, typeID))
                #print(tree+"test0"+str(test))
                #return test
            else:
                #same but difference for typeLenght = 1
                breaker=11
                number = int(padded_binary_original[bytePointer:bytePointer+breaker],2)
                bytePointer +=breaker
                lengthlimit -= breaker
                tempPointer = bytePointer
                #print(tree+"packagelength",number)
                test = bytesToNumber(subpackages=number,lengthlimit=lengthlimit)
                lengthlimit -= (bytePointer-tempPointer)
                #print(tree+"lenghtlimit1",lengthlimit)
                #print(tree+"Back from package",numbersArray)
                subpackages-=1
                numbersArray.append(applyId(test, typeID))
                #print(tree+"test1"+str(test),lengthlimit)
                #test
    
    
    #if there are numbers in test give back the numbers you calculated.
    print(tree+ "Return " + "test",test,"numbersarray",numbersArray)
    print(tree)
    tree = tree[1:]
    return numbersArray
part2=bytesToNumber(-1)
print("-------------------------------------\n\nPart:1",versionSum)
print("Part2:",part2)

