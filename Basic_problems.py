
'''
def Palindrome(arr):
    left=0
    right=len(arr)-1
    while left<right:
        if arr[left]!=arr[right]:
            return False
        left=left+1
        right-=1
    return True
print(Palindrome([1,2,3,3,2,1]))

def isPalindrome(arr,si,ei):
    if si>=ei:
        return
    if arr[si]!=arr[ei]:
        return False
    return isPalindrome(arr,si+1,ei-1)
arr=[1,2,3,3,2,1]
print(isPalindrome(arr,0,len(arr)-1))
'''
def Reverse(arr,si,ei):
    if si>=ei:
        return
    arr[si],arr[ei]=arr[ei],arr[si]
    return Reverse(arr,si+1,ei-1)
arr=[1,2,3,4,5]
Reverse(arr,0,len(arr)-1)
print(arr)
#Rotate the array left->right K times
def RotateArray(arr,k):
    Reverse(arr,0,len(arr)-1)
    Reverse(arr,0,k-1)
    Reverse(arr,k,len(arr)-1)
arr=[1,2,3,4,5]
RotateArray(arr,3)
print(arr)