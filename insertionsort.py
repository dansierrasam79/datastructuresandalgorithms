#Insertion Sort
def insertionSort(array,n):
    exch = 0
    for i in range(1,n):
        B = array[i]
        j = i
        while((j>0) and (array[j-1] > B)):
            array[j] = array[j-1]
            j-=1
            exch+=1
        array[j] = B
        exch=exch+1
    print(exch, " Exchanges during sorting")

#Main
i = 0
array = [12,9,4,99,120,1,3,10,23,45,75,69,31,88,101,14,29,91,2,0,77]
insertionSort(array,len(array))
print("Values after the sort:")
print(array)
