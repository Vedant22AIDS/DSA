def sum_of_digit(n):
    if n<10:
        return n
    else:
        return n%10+sum_of_digit(n//10)
print(sum_of_digit(111))

def power(a,n):
    if n==1:
        return a
    else:
        mid=n//2
        result=power(a,mid)
        final=result*result

        if n%2==0:
            return final
        else:
            return a*final
print(power(2,16))

def Print_array(arr,index):
    if index>=len(arr):
        return
    print(arr[index],end=" ")
    return Print_array(arr,index+1)

Print_array([1,2,3,4,5],0)
print()

def Print_Reverse_array(arr,index):
    if index>=len(arr):
        return
    return Print_array(arr,index+1)
    print(arr[index],end=" ")
Print_array([1,2,3,4,5],0)

print()
def smallest(arr,SI):
    if SI>=len(arr):
        return 9999999
    return min(arr[SI],smallest(arr,SI+1))
print(smallest([1,2,3,4,5],0))

print("Tower of Honoi")
print()
def moves(n,s,d,a):
    if n==1:
        return 1
    # move n-1 s->a,then move 1 biggest coin to s->d and then n-1 coin a-d
    return moves(n-1,s,a,d)+1+moves(n-1,a,d,s)
print(moves(1,'s','d','a'))
print(moves(2,'s','d','a'))
print(moves(3,'s','d','a'))
print(moves(4,'s','d','a'))

def Reverse(arr,si,ei):
    if si>ei:
        return
    arr[si],arr[ei]=arr[ei],arr[si]
    return Reverse(arr,si+1,ei-1)
arr=[1,2,3,4,5]
print(Reverse(arr,0,len(arr)-1))