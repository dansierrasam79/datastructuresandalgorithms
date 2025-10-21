# Dictionaries

def getDictValue(nDict):
    return nDict.get("Dream Theater")

def displayDict(nDict):
    print(nDict)

def addsDictItem(nDict):
    givenKey = input("Enter a key: ")
    givenValue = input("Enter a value: ")
    nDict[givenKey] = givenValue

def updateDictItem(nDict):
    givenKey = input("Enter a key: ")
    givenValue = input("Enter a value: ")
    nDict[givenKey] = givenValue

def removeDictItembyKey(nDict):
    givenKey = input("Enter a key: ")
    return nDict.pop(givenKey)

def removeRandomDictItem(nDict):
    return nDict.popitem()

def returndictValues(nDict):
    return nDict.values()

def returndictKeys(nDict):
    return nDict.keys()

def iterateDict(nDict):
    for k,v in nDict.items():
        print(k,v)

def sortDict(nDict):
    print(sorted(nDict))

if __name__ == "__main__":
    myDict = {"Bon Jovi": "Richie Sambora", "Guns N Roses": "Slash", "Dream Theater": "John Petrucci"}

    #Returns the value of key in dictionary
    getDictValue(myDict)

    # Adds a new key, value to the dictionary
    addsDictItem(myDict)
    print(myDict)

    # Updates the value of a particular key in the dictionary
    updateDictItem(myDict)
    print(myDict)

    # Removes item by value
    print(removeDictItembyKey(myDict))

    # Remove random dict item
    print(removeRandomDictItem(myDict))

    # Returns all dictionary values
    print(returndictValues(myDict))

    # Returns all dictionary keys
    print(returndictKeys(myDict))

    # Displays all keys and values in dictionary
    displayDict(myDict)

    # Iterates through all keys and values in dictionary
    iterateDict(myDict)

    # Sorts the dictionary
    sortDict(myDict)
