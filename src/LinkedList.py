from node import *

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        """ return string representation of linked list """
        s = "head-->"

        curr = self.head
        for i in range(self.size):
            s += ("(%s)"  %  str(curr.getItem()))
            curr = curr.getNext()

        s += ("<--tail")
        return s

    def __len__(self):
        return self.size

    def append(self, item): 
        """ add new node, containing item, to end of the list """
        n = Node(item)
        if self.size == 0:
            self.head = n
        else:
            self.tail.setNext(n)
            self.tail = n
            self.size += 1

    def prepend(self, item):
        """ add new node, containing item, to beginning of the list """
        n = Node(item)
        if self.size == 0:
            self.head = n
        else:
            n.setNext(self.head)
            self.head = n
            self.size += 1

    def deleteHead(self):
        self.head = self.head.getNext()
    
    def deleteTail(self):
        newTail = self.head
        for i in range(self.size - 1):
            newTail = newTail.getNext
        
        self.tail = newTail
        self.tail.getNext(None)

    def count(self, item):
        numNodes = 0

        curr = self.head
        for i in range(self.size):
            if curr.getItem() == item:
                numNodes += 1

            curr = curr.getNext()
        
        return numNodes

    def index(self, item):
        curr = self.head
        for i in range(self.size):
            if curr.getItem() == item:
                return i

            curr = curr.getNext()

    def insert(self, index, item):
        n = Node(item)
        if (index == 0):
            self.prepend(index)
        elif (index == self.size - 1):
            self.append(index)
        else:
            leftNode = None
            rightNode = None

            curr = self.head
            for i in range(index):
                curr = curr.getNext()

            leftNode = curr
            rightNode = curr.getNext()

            leftNode.setNext(n)
            n.setNext(rightNode)  

    def pop(self, index):
        if (index == 0):
            self.deleteHead()
        elif (index == self.size-1):
            self.deleteTail()
        else:
            leftNode = self.head
            for i in range(index-1):
                leftNode = leftNode.getNext()

            rightNode = leftNode.getNext().getNext()
            leftNode.setNext(rightNode)

    def remove(self, item):
        index = self.index(item)
        self.pop(index)

        
    
if __name__ == "__main__":		   # test the following methods: init, str, append, len
    LL = LinkedList()
    assert len(LL) == 0			    
    assert str(LL) == "head--><--tail"
    LL.append("A")
    LL.append("B")
    LL.append("C")
    assert len(LL) == 3
    assert str(LL) == "head→(A)(B)(C)<--tail"

