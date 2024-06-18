#Que1 Sorted array is rotated from left to right find how many number of times it is rotated

def Count_Rotation(arr):
    #Timicomlexity -> O(n)
    min_index=0
    for i in range(1,len(arr)):
        if(arr[min_index]>arr[i]):
            min_index=i
    return min_index

print(Count_Rotation([15,18,2,3,6,12]))

#Optimized Approch
def Count_Rotation_optimized(arr):
    for i in range(1,len(arr)):
        min_index=0
        if(arr[i]<arr[i-1] and arr[i]<arr[i+1]):
            min_index=i
            break
    return min_index
print(Count_Rotation_optimized([15,18,2,3,6,12]))

# More optimized approach - using binary search
def count_rotation(arr):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=left+(right-left)//2
        if arr[mid]<arr[mid-1] and arr[mid]<arr[mid+1]:
        #if arr[mid]<arr[left] and arr[mid]<arr[right]:
            return mid
        elif arr[mid]>arr[left]:
            right=mid-1
        else:
            left=mid+1
    return -1
print(count_rotation([6,12,15,18,2,3]))
print(count_rotation([4,5,1,2,3]))
print(count_rotation([12,15,18,2,3,6]))
print(count_rotation([4, 5, 6, 7, 1, 2, 3]))

#Que2 {8,1,6,2,5,3}->[l,s,l,s]
def array_pattern(arr):
    print("Array Pattern")
    for i in range(0,len(arr)-1):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[min_index]>arr[j]:
                arr[min_index],arr[j]=arr[j],arr[min_index]

    start=0
    end=len(arr)-1
    while start<=end:
        if start==end:
            print(arr[start])
        else:
            print(arr[end],arr[start],end=" ")
        start=start+1
        end=end-1
print(array_pattern([3,5,1,2,8,6,4]))

#Que3 sort array in wave form - first increasing and then decreasing
# {10,5,6,3,2,20,100,80} -> {10,5,6,3,20,2,100,80}
#similar to previous question

'''
def wave_form(arr):
    for i in range(0,len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    for i in range(1,len(arr),2):
        arr[i],arr[i+1]=arr[i+1],arr[i]
    print(arr)
arr=[1,2,5,10,23,49,90]
print(wave_form(arr))
'''

#optimized approach-
#don't consider first and lasst element
def wave_form(arr):
    for i in range(0,len(arr)-1,2):
        if i>0 and arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
        if i<len(arr)-1 and arr[i]>arr[i-1]:
            arr[i],arr[i - 1] = arr[i + 1],arr[i]
    print(arr)
arr=[10,90,49,2,1,5,23]
wave_form(arr)

#Que4 Merge array final array should be sorted
def mergeArray(arr1,m,arr2,n):
    i=m-1
    j=n-1
    k=m+n-1
    while(i>=0 and j>=0):
        if(arr1[i]>arr2[j]):
            arr1[k]=arr1[i]
            i-=1
        else:
            arr1[k]=arr2[j]
            j-=1
        k-=1
    while(i>=0):
        arr1[k]=arr1[i]
        k-=1
        i-=1
    while(j>=0):
        arr1[k]=arr2[j]
        k-=1
        j-=1
    print(arr1)
arr1=[3,6,8,-1,1]
arr2=[1,7]
mergeArray(arr1,3,arr2,2)