# Python program for implementation of Bubble Sort
def bubbleSort(arr):
    n = len(arr)
    swaps = 0
    #Traverse through all array elements
    for i in range(n-1, 0, -1):
        # Last i elements are already in place
        for j in range(0,i):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
            # return the number of swaps
    return swaps
# Driver code to test above
if __name__ == "__main__":
    myList = [12,9,4,99,120,1,3,10,23,45,75,69,31,88,101,14,29,91,2,0,77]
    swaptimes = bubbleSort(myList)
    print("Sorted array is: ", myList)

    print("Number of swaps: ", swaptimes)
