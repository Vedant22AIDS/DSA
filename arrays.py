# if we take external data structure then space complexity will increase. For new variables it will be constatns

def sum_arr(arr):
    # Time Complexity -O(n)
    # Space Complexity -O(1)
    sum = 0
    for i in range(len(arr)):
        sum=sum+arr[i]
    return sum

def search_element(arr,key):
    # Time Complexity -O(n)
    # Space Complexity -O(1)
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1

def even_odd(arr):
    # Time Complexity -O(n)
    # Space Complexity -O(n) value is propositonal to value of n
    even=[]
    odd=[]
    for i in range(len(arr)):
            if arr[i]%2==0:
                even.append(arr[i])
            else:
                odd.append(arr[i])
    return even,odd

arr=[1,2,3,4,5,6,7,8,9,10]
print(sum_arr(arr))
target=11
print(search_element(arr,target))
print(even_odd(arr))
