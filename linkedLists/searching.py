class SlinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node = self.head
        while node:
            yield node 
            node = node.next
    def traversalSLL(self):
        node = self.head
        while(node is not None):
            print(node)
            node = node.next
    def searching(self,nodeValue):
        if self.head == None:
            return "the list does not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return nodeValue
                node = node.next
            return "the value does not exist in the linked list" 
            

#step 2: create a node  that is blank and has a value to it and referenced to null

class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
singlyLinkedList = SlinkedList()

Node1 = Node(1)
Node2 = Node(2)

singlyLinkedList.head = Node1
singlyLinkedList.head.next = Node2
singlyLinkedList.tail = Node2
print(singlyLinkedList.searching(2))