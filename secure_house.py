#!/usr/bin/env python3
import sys

#init owner/keys from command arguments
owner = sys.argv[1]
keys = sys.argv
keys.remove("./secure_house")
keys.remove(owner)

splitLine = []
insertedKey = ""
userName = ""
isInside = False
houseMembers = []

#loop through stdin
for line in sys.stdin:
    splitLine.clear()
    splitLine = line.split(" ")
    if splitLine[0] == "INSERT" and splitLine[1] == "KEY":
        userName = splitLine[2]
        insertedKey = splitLine[3]
        insertedKey = insertedKey.rstrip()
        print('KEY '+insertedKey+' INSERTED BY '+userName)
    elif splitLine[0] == "TURN" and splitLine[1] == "KEY":
        attemptUser = splitLine[2].rstrip()
        if insertedKey in keys and userName == attemptUser:
            print("SUCCESS " + attemptUser + " TURNS KEY " + insertedKey)
            isInside = True
        else:
            print("FAILURE " + attemptUser + " UNABLE TO TURN KEY " + insertedKey)
    elif splitLine[0] == "ENTER" and splitLine[1] == "HOUSE":
        if splitLine[2].rstrip() == userName and isInside:
            print("ACCESS ALLOWED")
            houseMembers.append(userName)
        else:
            print("ACCESS DENIED")
    elif splitLine[0] == "WHO'S" and splitLine[1] == "INSIDE?\n":
        if not houseMembers:
            print("NOBODY HOME")
        else:
            print(*houseMembers, sep = ", ")
    elif splitLine[0] == "CHANGE" and splitLine[1] == "LOCKS":
        if splitLine [2] == owner:
            keys.clear()
            keys = splitLine.copy()
            keys.remove("CHANGE")
            keys.remove("LOCKS")
            keys.remove(owner)

            #last character will have \n
            keys[len(keys)-1] = keys[len(keys)-1].rstrip()
            print("OK")
        else:
            print("ACCESS DENIED")
    elif splitLine[0] == "LEAVE" and splitLine[1] == "HOUSE":
        if splitLine[2].rstrip() in houseMembers:
            houseMembers.remove(splitLine[2].rstrip())
            print("OK")
        else:
            print(splitLine[2].rstrip() + " NOT HERE")
    else:
        print("ERROR")
                
