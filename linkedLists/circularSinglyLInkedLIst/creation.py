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

CircularSlinkedList = CircularSlinkedList()
CircularSlinkedList.createCircularSlinkedlist(2)

print([node.value for node in CircularSlinkedList])