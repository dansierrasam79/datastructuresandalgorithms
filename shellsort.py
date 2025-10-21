# Shell Sort in Python

def shellSort(array, n):
    # Rearrange elements at each n/2, n/4, n/8... intervals
    interval = n//2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2

if __name__ == "__main__":
    array = [12,9,4,99,120,1,3,10,23,45,75,69,31,88,101,14,29,91,2,0,77]
    size = len(array)
    shellSort(array, size)
    print("Sorted array in ascending order: ", array)
