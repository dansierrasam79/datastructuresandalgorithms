def fibMonaccianSearch(arr, x, n):
    
    # Initialize fibonacci numbers
    fibMMm2 = 0 # (m-2)'th Fibonacci No
    fibMMm1 = 1 # (m-1)'th Fibonacci No
    fibM = fibMMm1 + fibMMm2
    # fibM is going to store the smallest Fibonacci Number greater than or equal to n
    while fibM < n:
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm1 + fibMMm2
    # Marks the eliminated range from front
    offset = -1
    # While there are elements to be inspected note that we compare arr[fibMMm2] with x. When fibM becomes 1 fibMMm2 becomes 0
    while fibM > 1:
        # Check if fibMMm2 is a valid location
        i = min(offset+fibMMm2, n-1)
        # If x is greater than the value at index fibMMm2, cut the subarray value from offset to i 
        if arr[i] < x:
            fibM = fibMMm2
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i
        # If x is less than the value at index fibMMm2, cut the subarray after i + 1
        elif arr[i] > x:
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1
        # Element found. Return index
        else:
            return i
        # comparing the last element with x
        if fibMMm1 and arr[n-1] == x:
            return n-1
        # Element not found return -1
        return -1
        
# Driver code
if __name__ == "__main__":
    arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100, 235]
    n = len(arr)
    x = 255
    ind = fibMonaccianSearch(arr, x, n)
    if ind >= 0:
        print("Found at index: ", ind)
    else:
        print(x, "is not present in the array")
        
