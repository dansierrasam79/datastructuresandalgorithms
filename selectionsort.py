def selectionSearch(arr):
    swaps = 0
    # Traverse through all array elements
    for i in range(0,len(arr)):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        # Swap the found minimum element with first element
        arr[i], arr[min_idx] = arr[min_idx],arr[i]
        swaps += 1
    return swaps

# Driver code
if __name__ == "__main__":
    myList = [12,9,4,99,120,1,3,10,23,45,75,69,31,88,101,14,29,91,2,0,77]
    swaptimes = selectionSearch(myList)
    print(myList)
    print(swaptimes)
