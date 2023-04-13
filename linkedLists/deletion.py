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
    def deleteNode(self,location):
        if self.head is None:
            return "the Linked list does not exist"
        else:
            if(location == 0 ):
                if self.head == self.tail:
                    self.head == None 
                    self.tail == None
                else:
                    self.head == self.head.next 
            elif(location == -1 ):
                if self.head == self.tail:
                    self.head == None 
                    self.tail == None
                else:
                    node= self.head 
                    while node is not None:
                        if node.next ==self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node 
            else:
                tempNode = self.head
                index=0 
                while index < location -1:
                    tempNode = tempNode.next
                    index+=1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
    def deleteEntireSLL(self):
        if self.head == None:
            print("the ll doesnt exist")
        else:
            self.head = None
            self.tail= None 
                
            

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