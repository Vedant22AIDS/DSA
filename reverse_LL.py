class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

def traverse(head):
    while head:
        print(head.getData(), end="->")
        head = head.getNext()
    print("None")

def reverse(head):
    prev=None
    current=head
    while current:
        next=current.getNext()
        current.setNext(prev)
        prev=current
        current=next
    return prev

head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

head.setNext(node2)
node2.setNext(node3)
node3.setNext(node4)
node4.setNext(node5)

print("Original list:")
traverse(head)

reversed_head = reverse(head)
print("Reversed list:")
traverse(reversed_head)





