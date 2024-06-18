def remove_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                arr.pop(j)
    print(arr)
arr = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5]
print(remove_duplicate(arr))