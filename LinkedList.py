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

def traversal(head):
    while head:
        print(head.getData(),end="->")
        head=head.getNext()
    print("None")

def rec_traversal(head):
    if head:
        print(head.getData(),end="->")
        rec_traversal(head.getNext())

def length(head):
    i=0
    while head:
        i+=1
        head=head.getNext()
    return i

def rec_length(head):
    if not head:
        return 0
    else:
        return 1+rec_length(head.getNext())

#Insertion Operation
def insertNode(head,data,k):
    if(k<0 or length(head)<k):
        print("Invalid value of k")
        return head
    newNode = Node(data)
    if k==0:
        newNode.setNext(head)
        head=newNode
    else:
        i=0
        prev=head
        while i<k-1:
            prev=prev.getNext()
            i+=1
        newNode.setNext(prev.getNext())
        prev.setNext(newNode)
    return head

#Deletion Operation
def DeleteNode(head,k):
    if (k < 0 or k >= length(head) or not head):
        return head

    if (k == 0):
        # We are removing the first element
        head = head.getNext()
    else:

        # We jump to k-1th position
        i = 0
        prev = head
        while (i < k - 1):
            prev = prev.getNext()
            i += 1
        # prev will be pointing to the node left of the kth position
        prev.setNext(prev.getNext().getNext())

    return head


head=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)

head.setNext(node2)
node2.setNext(node3)
node3.setNext(node4)
node4.setNext(node5)

traversal(head)
rec_traversal(head)
length(head)
print(rec_length(head))

print()
print("Insertion at beginning")
head=insertNode(head,3,0)
traversal(head)

print()

print("Insertion at end")
head=insertNode(head,5,5)
traversal(head)

print()

print("Invalid Case")
head=insertNode(head,5,125)
traversal(head)

print()
print("Deletion at beginning")
head=DeleteNode(head,0)
traversal(head)

print()

print("Deletion at end")
head=DeleteNode(head,5)
traversal(head)
print()

