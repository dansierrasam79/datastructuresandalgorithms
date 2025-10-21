#quicksort algorithm
# Quick sort in Python
# Function to partition the array on the basis of pivot element
array2 = []
def partition(array, low, high):

# Select the pivot element
    pivot = array[high]
    i = low - 1
# Put the elements smaller than pivot on the left and greater than pivot on the right of pivot
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return (i + 1)

def quickSort(array, low, high):
    print(array[low:high])
    if low < high:
# Select pivot position and put all the elements smaller than pivot on left and greater than pivot on right
        pi = partition(array, low, high)
# Sort the elements on the left of pivot
        quickSort(array, low, pi - 1)

# Sort the elements on the right of pivot
        quickSort(array, pi + 1, high)
#Driver code
data = [12,9,4,99,120,1,3,10,23,45,75,69,31,88,101,14,29,91,2,0,77]
total = 0
#[8, 7, 2, 1, 0, 9, 6]
size = len(data)
quickSort(data, 0, size - 1)
print('Sorted Array in Ascending Order:')
print(data)
