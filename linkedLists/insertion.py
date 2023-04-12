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
    def insertSLinkedList(self, value , location):
        newNode=Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None 
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head 
                index = 0 
                while index < location -1 :
                    tempNode =  tempNode.next
                    index+=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode 




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
singlyLinkedList.insertSLinkedList(1,1)
print([node.value for node in singlyLinkedList])