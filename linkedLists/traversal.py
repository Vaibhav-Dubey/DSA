#steps for creating a singly linked list 

#step 1 : create a head and tail and initialise with null 


class SlinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node = self.head
        while node:
            yield node 
            node = node.next
    def traverseSLL(self):
        if self.head == None:
            print("The single Linked List does not exist")
        else:
            node = self.head
            while(node is not None):
                print(node.value)
                node = node.next


#step 2: create a node  that is blank and has a value to it and referenced to null

class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

#step  3 link head and tail to nodes 

singlyLinkedList = SlinkedList()

Node1 = Node(1)
Node2 = Node(2)

singlyLinkedList.head = Node1
singlyLinkedList.head.next = Node2
singlyLinkedList.tail = Node2

print([node.value for node in singlyLinkedList])

singlyLinkedList.traverseSLL()