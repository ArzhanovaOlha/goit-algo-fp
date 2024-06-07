class Node:

    def __init__(self, data = None, next=None): 
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data)
            temp = temp.next
    
    def insertionSortList(self):
        
        current = self.head
        for _ in range(self.length-1):
            temp_node = current.next
            while temp_node:
                if temp_node.data < current.data:
                    current.data, temp_node.data = temp_node.data, current.data
                temp_node = temp_node.next
            current = current.next
        return self 

def merge(llist1, llist2):
    head_ptr = temp_ptr = Node()
    
    while llist1 or llist2:
        if llist1 and (not llist2 or llist1.data <= llist2.data):
            temp_ptr.next = Node(llist1.data)
            llist1 = llist1.next
        else:
            temp_ptr.next = Node(llist2.data)
            llist2 = llist2.next
        temp_ptr = temp_ptr.next
    return head_ptr.next

llist1 = LinkedList()
llist1.push(17)
llist1.push(25)
llist1.push(1)
llist1.push(8)

llist2 = LinkedList()
llist2.push(4)
llist2.push(7)
llist2.push(10)
llist2.push(3)

print ("\nGiven Linked List")
llist1.printList()
llist1.reverse()
print ("\nReversed Linked List")
llist1.printList()

print("\nLinked List before sorting ")
llist2.printList()
a = llist2.insertionSortList()
print("\nLinked List after sorting ")
a.printList()

b = llist1.insertionSortList()

c = LinkedList()
c.head=merge(a.head, b.head)
print("\nMarge of two sorted linked lists")
c.printList()
