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
            self.tail = n
        else:
            self.tail.setNext(n)
            self.tail = n
        self.size += 1

    def prepend(self, item):
        """ add new node, containing item, to beginning of the list """
        n = Node(item)
        if self.size == 0:
            self.head = n
            self.tail = n
        else:
            n.setNext(self.head)
            self.head = n
        self.size += 1

    def deleteHead(self):
        prevHead = self.head

        if self.size == 0:
            return None 
        elif self.size == 1: 
            self.head = None 
            self.tail = None 
        else:
            self.head = prevHead.getNext()
            
        self.size -= 1
        return prevHead.getItem()
    
    def deleteTail(self):
        prevTail = self.tail

        if self.size == 0:
            return None 
        elif self.size == 1: 
            self.head = None 
            self.tail = None 
        else: 
            newTail = self.head
            for i in range(self.size - 1):
                newTail = newTail.getNext()
            self.tail = newTail

        self.size -= 1
        return prevTail.getItem()


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

        return -1

    def insert(self, index, item):
        n = Node(item)

        if (index == 0):
            self.prepend(item)
        elif (index >= self.size):
            self.append(item)
        else:
            curr = self.head
            for i in range(index-1):
                curr = curr.getNext()

            prevNode = curr
            nextNode = curr.getNext()

            prevNode.setNext(n)
            n.setNext(nextNode)  
            self.size += 1

    def pop(self, index):
        if (index == 0):
            return self.deleteHead()
        elif (index == self.size):
            return self.deleteTail()
        else:
            prevNode = self.head
            for i in range(index-1):
                prevNode = prevNode.getNext()

            middleNode = prevNode.getNext()
            nextNode = middleNode.getNext()
            prevNode.setNext(nextNode)
            self.size -= 1

            return middleNode.getItem()

    def remove(self, item):
        index = self.index(item)
        if (index == -1): 
            return None
        else:
            return self.pop(index)

        #TODO: write and raise errors

        
    
if __name__ == "__main__":		   # test the following methods: init, str, append, len
    LL = LinkedList()
    assert len(LL) == 0			    
    assert str(LL) == "head--><--tail"
    LL.append("A")
    LL.append("B")
    LL.append("C")
    assert len(LL) == 3
    assert str(LL) == "head-->(A)(B)(C)<--tail"
    
    LL.prepend("A")
    LL.prepend("B")
    LL.prepend("C")
    assert len(LL) == 6
    assert str(LL) == "head-->(C)(B)(A)(A)(B)(C)<--tail"

    LL.deleteHead()
    assert len(LL) == 5
    assert str(LL) == "head-->(B)(A)(A)(B)(C)<--tail"

    LL.deleteTail()
    assert len(LL) == 4
    assert str(LL) == "head-->(B)(A)(A)(B)<--tail"


    assert LL.count("A") == 2
    assert LL.count("B") == 2

    assert LL.index("A") == 1
    assert LL.index("B") == 0

    LL.insert(2, "C")
    assert str(LL) == "head-->(B)(A)(C)(A)(B)<--tail"

    LL.pop(0)
    LL.pop(0)
    assert str(LL) == "head-->(C)(A)(B)<--tail"

    LL.remove("A")
    assert str(LL) == "head-->(C)(B)<--tail"
    



