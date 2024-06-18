def Linear_Search(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1

print(Linear_Search([33,11,6,78,45,12],12))

def Binary_Search(arr,key):
    l = 0
    r = len(arr)-1
    while(l<=r):
        mid=(l+r)//2
        if key==arr[mid]:
            return mid
        elif key>arr[mid]:
            l=mid+1
        else:
            r=mid-1
    return -1

arr=[2,3,8,10,16]
print(Binary_Search(arr,10))

#Linear Search using recursion
def Linear_Search_recursion(arr,size,key):
    if size<0:
        return -1
    if key==arr[size-1]:
        return size-1
    else:
       return Linear_Search_recursion(arr,size-1,key)
arr=[1,2,3,4,5,6,7,8,9,10]
print(Linear_Search_recursion(arr,len(arr),1))

# Binary search using recursion
def Binary_Search_recursion(arr,l,r,key):
    if l>r:
        return -1

    mid=l+(r-l)//2
    if key==arr[mid]:
        return mid
    if key>arr[mid]:
        return Binary_Search_recursion(arr,mid+1,r,key)
    else:
      return Binary_Search_recursion(arr,l,mid-1,key)
arr=[12,13,14,16,18]
print(Binary_Search_recursion(arr,0,len(arr)-1,18))

