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


def merge_list(head1, head2):
    dummy = Node()
    tail = dummy

    while head1 and head2:
        if head1.getData() < head2.getData():
            tail.setNext(head1)
            head1 = head1.getNext()
        else:
            tail.setNext(head2)
            head2 = head2.getNext()
        tail = tail.getNext()

    if head1:
        tail.setNext(head1)

    if head2:
        tail.setNext(head2)
    return dummy.getNext()
head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

head.setNext(node2)
node2.setNext(node3)
node3.setNext(node4)
node4.setNext(node5)

print("Linked list 1:")
traverse(head)

head2 = Node(6)
n2 = Node(7)
n3 = Node(8)
n4 = Node(9)
n5 = Node(10)

head2.setNext(n2)
n2.setNext(n3)
n3.setNext(n4)
n4.setNext(n5)
print("Linked list 2:")
traverse(head2)

merge_head=merge_list(head,head2)
print("Merged Sorted Linked List :")
traverse(merge_head)




