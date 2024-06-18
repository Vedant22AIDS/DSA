class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

    def setData(self,data):
        self.data=data

    def getData(self):
        return self.data

    def setNext(self,next):
        self.next = next

    def getNext(self):
        return self.next

def rec_traversal(head):
    if head:
        print(head.getData(),end="->")
        rec_traversal(head.getNext())

#Finding Middle Element

def MiddleNode(head):
   fast=head
   slow=head
   while fast!=None and fast.getNext()!=None:
         fast=fast.getNext().getNext()
         slow=slow.getNext()
   return slow.getData()

#Cycle Detection Problem
def isCyclePresent(head):
  slow = head
  fast = head

  while(fast and fast.getNext()):
    slow = slow.getNext()
    fast = fast.getNext().getNext()

    if fast and slow.getData() == fast.getData():
      return True #cycle exists

  return False #Cycle doesn't exist

def searching(head,element):
    while head:
        if head.getData()==element:
            return True
        else:
            head=head.getNext()
    return False

head=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)

head.setNext(node2)
node2.setNext(node3)
node3.setNext(node4)
node4.setNext(node5)


print(rec_traversal(head))
print("Middle Element : ",MiddleNode(head))
print("Cycle :",isCyclePresent(head))

n=int(input("Enter a number to be search in linked list : "))
print("Element Present : ",searching(head,n))