def diagonal_sum(arr):
#Time Complexity : O(n^2)
#Space Complexity : O(1)
    primarydiagonalSum=0
    secondarydiagonalSum = 0
    n=len(arr)
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                primarydiagonalSum=primarydiagonalSum+arr[i][j]
            if ((i+j)==(n-1)):
                secondarydiagonalSum=secondarydiagonalSum+arr[i][j]
    print("Primary Diagonal Sum :",primarydiagonalSum)
    print("Secondary Diagonal Sum :", secondarydiagonalSum)

arr=[[2,4,6],[8,11,13],[14,17,19]]
print(diagonal_sum(arr))