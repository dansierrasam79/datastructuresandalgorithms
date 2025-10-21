# Lists

def insertElement(nList):
    newItem = int(input("Enter an element"))
    nList.append(newItem)
    return nList

def insertElementAtLocation(nList):
    newItem = int(input("Enter an element: "))
    position = int(input("Enter the position: "))
    nList.insert(position, newItem)

def removeElement(nList):
    removedItem = int(input("Enter the element: "))
    nList.remove(removedItem)

def returnIndexofItem(nList):
    newItem = int(input("Enter an element"))
    return nList.index(newItem)

def reversesList(nList):
    nList.reverse()

def sortList(nList):
    nList.sort()

def countIteminList(nList):
    return nList.count(2)

def MergesLists(nList, mList):
    return nList.extend(mList)

def removeElementatIndex(nList):
    position = int(input("Enter the index position: "))
    nList.pop(position)

def copiesItemsIntoList(nList):
    mList = nList.copy()
    return mList

if __name__ == "__main__":
    aList = [1,2,3,4,5,2,6,7,8,9,10]
    bList = [11,12,13]
    
    # Inserts an element into a list
    insertElement(aList)
    print(aList)

    # Inserts an element into a particular position of the list
    insertElementAtLocation(aList)
    print(aList)

    # Removes an element from a list
    removeElement(aList)
    print(aList)

    # Returns index of list
    print(returnIndexofItem(aList))

    # Reverses a list
    reversesList(aList)
    print(aList)

    # Sorts the list
    sortList(aList)
    print(aList)

    # Counts item in list
    print(countIteminList(aList))
    
    # Extends the list with another list or merges two lists
    MergesLists(aList, bList)
    print(aList)

    # Removes element at a particular index in a list
    removeElementatIndex(aList)
    print(aList)

    # Copies items of a list into another
    print(copiesItemsIntoList(aList))
