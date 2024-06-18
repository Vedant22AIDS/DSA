#Bubble_sort
def Bubble_sort(arr):
    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
print(Bubble_sort([5,4,3,2,1]))

def Bubble_sort_Optimized(arr):
    for i in range(len(arr)):
        isSorted=True
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                isSorted=False
                arr[j],arr[j+1]=arr[j+1],arr[j]
        if isSorted:
            break
    return arr
print(Bubble_sort_Optimized([1,2,3,4,5]))
print(Bubble_sort_Optimized([19,21,44,11,5,7]))

def isSorted(arr):
    isSorted=True
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            isSorted=False
            break
    if isSorted:
        print("Array is already sorted")
    else:
        print("Array is not sorted")
print(isSorted([1,2,3,4,5]))
print(isSorted([1,7,3,4,5]))

print()
print("selection sort")
def selection_sot(arr):
    for i in range(len(arr)-1):
        min_val=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_val]:
                arr[min_val],arr[j]=arr[j],arr[min_val]
    return arr
print(selection_sot([3,1,4,6,11,7]))

#Insertion Sort
def Insertion_Sort(arr):
    for i in range(1,len(arr)):
        v=arr[i]
        j=i
        while(j>=0 and arr[j-1]>arr[i]):
            arr[j]=arr[j-1]
            j=j-1
        arr[j]=v
    return arr
print("Insertion Sort :",Insertion_Sort([2,5,3,8,4]))
