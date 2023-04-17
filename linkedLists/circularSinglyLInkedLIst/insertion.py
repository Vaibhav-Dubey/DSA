class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None


class CircularSlinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node = self.head
        while node:
            yield node 
            if node.next == self.head:
                break
            node = node.next
    def createCircularSlinkedlist(self,nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node 
        return "the CSLL has been created"
    def insertCSLL(self,value, location):
        if self.head == None:
            return "the head value is none"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head 
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.tail.next
                self.tail.next =  newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0 
                while index < location-1:
                    tempNode = tempNode.next
                    index+=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return "the node has been inserted"

CircularSlinkedList = CircularSlinkedList()
CircularSlinkedList.createCircularSlinkedlist(2)
CircularSlinkedList.insertCSLL(0,0)

print([node.value for node in CircularSlinkedList])