# Tuples

def findIndexofElement(nTuple):
    findItem = int(input("Enter the item: "))
    return nTuple.index(findItem)

def countItemsinTuple(nTuple):
    countItem = int(input("Enter the item: "))
    return nTuple.count(countItem)

if __name__ == "__main__":
    aTuple = (1,2,3,4,5,6,7,8,2,9,10)
    # Find the index number of an element in a tuple
    print(findIndexofElement(aTuple))
    
    # Finds how many times an elements exists in a tuple
    print(countItemsinTuple(aTuple))
