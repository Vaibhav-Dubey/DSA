from linkedListClass import LinkedList


def removeDups(l1):
    if l1.head == None:
        return 
    else:
        curNode = l1.head
        visited = set([curNode.value])
        while curNode.next:
            if curNode.next.value in visited:
                curNode.next = curNode.next.next
            else:
                visited.add(curNode.next.value)
        return l1
    

customLL = LinkedList()
customLL.add(10)
customLL.add(10)
customLL.add(10)
print(customLL)
print(removeDups(customLL))