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

#Find the starting point of the loop
def startingPointOfCycle(head):
    slow=head
    fast=head
    iscyclePresent=False

    while fast!=None and fast.getNext()!=None:
        slow=slow.getNext()
        fast=fast.getNext().getNext()

        if slow.getData()==fast.getData() and fast!=None:
            iscyclePresent=True
            print("Cycle Present :",iscyclePresent)
            break
    if not iscyclePresent:
        return False

    temp=head
    while temp.getData()!=slow.getData():
        temp=temp.getNext()
        slow=slow.getNext()
    return temp.getData()

head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

#Creating the linkage
head.setNext(node2)
node2.setNext(node3)
node3.setNext(node4)
node4.setNext(node5)
node5.setNext(node6)
node6.setNext(node3)

print(startingPointOfCycle(head))

