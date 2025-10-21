# Sets

def displaySet(mSet):
    print(mSet)

def addItemstoSet(mSet):
    givenValue = input("Enter a given value: ")
    mSet.add(givenValue)

def updateSetItems(mSet):
    mSet.update([11,12,13], {14,15,16})

def removeSetElements(mSet):
    givenValue = int(input("Enter a given value: "))
    mSet.remove(givenValue)

def removeSetElements2(mSet):
    givenValue = int(input("Enter a given value: "))
    mSet.discard(givenValue)

def removerandomElement(mSet):
    mSet.pop()

if __name__ == "__main__":
    mySet = {1,2,3,4,5}
    mySet2 = {5,6,7,8,9,10}
    # Displays all items in the set
    displaySet(mySet)
    
    # Adds items to set
    addItemstoSet(mySet)
    print(mySet)
    
    # Updates items in set
    updateSetItems(mySet)
    print(mySet)

    # Removes set elements by element
    removeSetElements(mySet)
    print(mySet)

    # Removes set elements by element
    removeSetElements(mySet)
    print(mySet)

    # Removes random element from set
    removerandomElement(mySet)
    print(mySet)

    # Union operation A | B
    print(mySet.union(mySet2))

    # Intersection operation mySet & mySet2
    print(mySet.intersection(mySet2))
    
    # Set difference A - B 
    print(mySet.difference(mySet2))

    # Symmetric difference A ^ B
    print(mySet.symmetric_difference(mySet2))
