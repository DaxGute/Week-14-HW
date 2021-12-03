from node import *

class LinkedList:
    """ a class to implement a linked list. A linked list is a linear collection of data elements 
    whose order is not given by their physical placement in memory """

    def __init__(self):

        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        """ return string representation of linked list (returns string)"""
        s = "head-->"

        curr = self.head
        for i in range(self.size):
            s += ("(%s)"  %  str(curr.getItem()))
            curr = curr.getNext()

        s += ("<--tail")
        return s

    def __len__(self):
        """ return the length of the linked list (returns int)"""
        return self.size

    def __contain__(self, value):
        """ returns true if value is contained in list (return boolean) """
        listContains = False
        curr = self.head
        for i in range(self.size):
            if curr.getItem() == value:
                listContains = True
            curr = curr.getNext()

        return listContains
        
    def __getitem__(self, index):
        """ return the item at the given index (returns node item (typically string)) """
        if index < 0:
            index = self.size + index
            if index < 0:
                raise IndexError("list index out of range")
        elif index >= self.size:
            raise IndexError("list index out of range")

        curr = self.head
        for i in range(index):
            curr = curr.getNext()
        
        itemValue = curr.getItem()
        return itemValue

    def __setitem__(self, index, value):
        """ sets the item at the given index """
        if index < 0:
            index = self.size + index
            if index < 0:
                raise IndexError("list index out of range")
        elif index >= self.size:
            raise IndexError("list index out of range")

        curr = self.head
        for i in range(index):
            curr = curr.getNext()
        
        curr.setItem(value)
        return
    
    def isEmpty(self):
        """ return a boolean flag indicating whether the list is empty or not (returns boolean) """
        isEmpty = False
        if self.size == 0:
            isEmpty = True
        return isEmpty 
        
    def append(self, item): 
        """ add new node, containing item, to end of the list """
        n = Node(item)
        if self.isEmpty():
            self.head = n
            self.tail = n
        else:
            self.tail.setNext(n)
            self.tail = n
        self.size += 1
        return  

    def prepend(self, item):
        """ add new node, containing item, to beginning of the list """
        n = Node(item)
        if self.isEmpty():
            self.head = n
            self.tail = n
        else:
            n.setNext(self.head)
            self.head = n
        self.size += 1
        return 

    def deleteHead(self):
        """ delete the head node, return item stored in deleted node (returns node item (typically string)) """
        headItem = None
        prevHead = self.head

        if not self.isEmpty():
            if self.size == 1: 
                self.head = None 
                self.tail = None 
            else:
                self.head = prevHead.getNext()
            headItem = prevHead.getItem()
            self.size -= 1

        return headItem
    
    def deleteTail(self):
        """ delete the tail node, return item stored in deleted node (returns node item (typically string)) """
        tailItem = None
        prevTail = self.tail

        if not self.isEmpty():
            if self.size == 1: 
                self.head = None 
                self.tail = None 
            else: 
                newTail = self.head
                for i in range(self.size - 2):
                    newTail = newTail.getNext()
                self.tail = newTail
                self.tail.setNext(None)
            tailItem = prevTail.getItem()
            self.size -= 1

        return tailItem


    def count(self, item):
        """ count and return the number of nodes that contain item (return int) """
        numNodes = 0
        curr = self.head
        for i in range(self.size):
            if curr.getItem() == item:
                numNodes += 1
            curr = curr.getNext()
        return numNodes

    def index(self, item):
        """ return the index of the first node that contains item (returns int) """
        curr = self.head
        for i in range(self.size):
            if curr.getItem() == item:
                return i
            curr = curr.getNext()
        raise ValueError("'" + item + "' is not in list")

    def insert(self, index, item):
        """ insert node containing item at given index """
        n = Node(item)

        if index >= self.size:
            self.append(item)
        else:
            if index < 0:
                index = self.size + index
                if index < 0:
                    index = 0
            
            if index == 0:
                self.prepend(item)
            else:
                curr = self.head
                for i in range(index-1):
                    curr = curr.getNext()

                prevNode = curr
                nextNode = curr.getNext()

                prevNode.setNext(n)
                n.setNext(nextNode)  
                self.size += 1
        return

    def pop(self, index):
        """ remove and return item at index (returns node item (typically string)) """
        popItem = None

        if self.isEmpty():
            raise IndexError("pop from empty list")
        elif index < self.size:
            if index < 0:
                index = self.size + index
                if index < 0:
                    raise IndexError("pop index out of range")
            if index == 0:
                popItem = self.deleteHead()
            elif index == self.size-1:
                popItem = self.deleteTail()
            else:
                curr = self.head
                for i in range(index-1):
                    curr = curr.getNext()

                prevNode = curr
                middleNode = curr.getNext()
                nextNode = middleNode.getNext()
                prevNode.setNext(nextNode)

                self.size -= 1
                popItem = middleNode.getItem()
        else:
            raise IndexError("pop index out of range")

        return popItem

    def remove(self, item):
        """ remove first instance of item in list """
        currNode = self.head

        if currNode.getItem() == item:
            self.deleteHead()
        elif self.head.getItem() == item:
            self.deleteTail()
        else:
            prevNode = currNode
            foundItem = False
            for i in range(self.size - 2):
                midNode = prevNode.getNext()
                if midNode.getItem() == item:
                    nextNode = midNode.getNext()
                    prevNode.setNext(nextNode)
                    self.size -= 1
                    foundItem = False
                prevNode = prevNode.getNext()
            
            if foundItem == False:
                raise ValueError("list.remove(x): x not in list")

        return
        
    
if __name__ == "__main__":		   # test the following methods: init, str, append, len
    L=[]
    L.append("a")
    print(L.remove("a"))
    LL = LinkedList()
    """ Testing isEmpty() Method"""
    assert LL.isEmpty() == True
    LL.append("A")
    assert LL.isEmpty() == False
    LL.remove("A")
    assert LL.isEmpty() == True

    LL = LinkedList()
    """ Testing len() Method """
    assert len(LL) == 0
    LL.append("A")
    assert len(LL) == 1
    LL.prepend("B")
    assert len(LL) == 2
    LL.deleteHead()
    assert len(LL) == 1
    LL.append("A")
    assert len(LL) == 2
    LL.deleteTail()
    assert len(LL) == 1
    LL.append("A")
    assert len(LL) == 2
    LL.prepend("B")
    assert len(LL) == 3
    LL.pop(1)
    assert len(LL) == 2
    LL.remove("A")
    assert len(LL) == 1

    LL = LinkedList()
    """ Testing str() Method """
    assert str(LL) == "head--><--tail"
    LL.append("A")
    assert str(LL) == "head-->(A)<--tail"
    LL.prepend("B")
    assert str(LL) == "head-->(B)(A)<--tail"
    LL.deleteHead()
    assert str(LL) == "head-->(A)<--tail"
    LL.append("B")
    assert str(LL) == "head-->(A)(B)<--tail"
    LL.deleteTail()
    assert str(LL) == "head-->(A)<--tail"
    LL.append("C")
    assert str(LL) == "head-->(A)(C)<--tail"
    LL.prepend("B")
    assert str(LL) == "head-->(B)(A)(C)<--tail"
    LL.pop(1)
    assert str(LL) == "head-->(B)(C)<--tail"
    LL.remove("C")
    assert str(LL) == "head-->(B)<--tail"

    LL = LinkedList()
    """ Testing append() Method """
    LL.append("A")
    assert str(LL) == "head-->(A)<--tail"
    LL.append("B")
    assert str(LL) == "head-->(A)(B)<--tail"
    LL.append("C")
    assert str(LL) == "head-->(A)(B)(C)<--tail"
    assert len(LL) == 3
    LL.pop(0)
    LL.pop(0)
    LL.pop(0)
    LL.append("B")
    assert str(LL) == "head-->(B)<--tail"
    LL.append("C")
    assert str(LL) == "head-->(B)(C)<--tail"

    LL = LinkedList()
    """ Testing prepend() Method """
    LL.prepend("A")
    assert str(LL) == "head-->(A)<--tail"
    LL.prepend("B")
    assert str(LL) == "head-->(B)(A)<--tail"
    LL.prepend("C")
    assert str(LL) == "head-->(C)(B)(A)<--tail"
    assert len(LL) == 3
    LL.pop(0)
    LL.pop(0)
    LL.pop(0)
    LL.prepend("B")
    assert str(LL) == "head-->(B)<--tail"
    LL.prepend("C")
    assert str(LL) == "head-->(C)(B)<--tail"

    LL = LinkedList()
    """ Testing deleteHead() Method """
    assert LL.deleteHead() == None
    assert str(LL) == "head--><--tail" 
    LL.append("A")
    LL.append("B")
    LL.append("C")
    assert LL.deleteHead() == "A"
    assert str(LL) == "head-->(B)(C)<--tail" 
    assert LL.deleteHead() == "B"
    assert str(LL) == "head-->(C)<--tail" 
    assert LL.deleteHead() == "C"
    assert str(LL) == "head--><--tail" 

    LL = LinkedList()
    """ Testing deleteTail() Method """
    assert LL.deleteTail() == None
    assert str(LL) == "head--><--tail" 
    LL.append("A")
    LL.append("B")
    LL.append("C")
    assert LL.deleteTail() == "C"
    assert str(LL) == "head-->(A)(B)<--tail" 
    assert LL.deleteTail() == "B"
    assert str(LL) == "head-->(A)<--tail" 
    assert LL.deleteTail() == "A"
    assert str(LL) == "head--><--tail" 

    LL = LinkedList()
    """ Testing count() Method """
    assert LL.count("C") == 0
    LL.append("A")
    LL.append("B")
    assert LL.count("C") == 0
    LL.append("C") 
    assert LL.count("C") == 1
    LL.append("A")
    LL.append("B")
    assert LL.count("C") == 1
    LL.append("C") 
    assert LL.count("C") == 2
    LL.pop(2)
    assert LL.count("C") == 1

    LL = LinkedList()
    """ Testing index() Method """
    LL.append("A")
    LL.append("B")
    assert LL.index("A") == 0
    LL.append("C")
    assert LL.index("C") == 2
    LL.append("A")
    LL.append("B")
    LL.append("C")
    assert LL.index("C") == 2
    LL.pop(2)
    assert LL.index("C") == 4

    LL = LinkedList()
    """ Testing insert() Method """
    LL.insert(0, "A")
    assert str(LL) == "head-->(A)<--tail"
    LL.pop(0)
    LL.insert(-1, "A")
    assert str(LL) == "head-->(A)<--tail"
    LL.pop(0)
    LL.insert(2, "A")
    assert str(LL) == "head-->(A)<--tail"
    LL.insert(-1, "B")
    assert str(LL) == "head-->(B)(A)<--tail"
    LL.insert(4, "C")
    assert str(LL) == "head-->(B)(A)(C)<--tail"
    LL.insert(-2, "D")
    assert str(LL) == "head-->(B)(D)(A)(C)<--tail"
    LL.insert(4, "E")
    assert str(LL) == "head-->(B)(D)(A)(C)(E)<--tail"
    LL.insert(-100, "F")
    assert str(LL) == "head-->(F)(B)(D)(A)(C)(E)<--tail"

    LL = LinkedList()
    """ Testing pop() Method """
    LL.append("A")
    LL.append("B")
    LL.append("C")
    LL.append("D")
    LL.append("E")
    LL.append("F")
    assert LL.pop(0) == "A"
    assert str(LL) == "head-->(B)(C)(D)(E)(F)<--tail"
    assert LL.pop(3) == "E"
    assert str(LL) == "head-->(B)(C)(D)(F)<--tail"
    assert LL.pop(-2) == "D"
    assert str(LL) == "head-->(B)(C)(F)<--tail"
    assert LL.pop(1) == "C"
    assert str(LL) == "head-->(B)(F)<--tail"
    assert LL.pop(1) == "F"
    assert str(LL) == "head-->(B)<--tail"
    assert LL.pop(0) == "B"
    assert str(LL) == "head--><--tail"

    LL = LinkedList()
    """ Testing remove() Method """
    LL.append("A")
    LL.append("B")
    LL.append("C")
    LL.append("A")
    LL.append("D")
    LL.append("E")
    assert str(LL) == "head-->(A)(B)(C)(A)(D)(E)<--tail"
    LL.remove("A")
    assert str(LL) == "head-->(B)(C)(A)(D)(E)<--tail"
    LL.remove("A")
    assert str(LL) == "head-->(B)(C)(D)(E)<--tail"
    LL.remove("E")
    assert str(LL) == "head-->(B)(C)(D)<--tail" 
    LL.remove("C")
    assert str(LL) == "head-->(B)(D)<--tail" 
    LL.remove("B")
    assert str(LL) == "head-->(D)<--tail" 
    LL.remove("D")
    assert str(LL) == "head--><--tail" 

    LL = LinkedList()
    """ Testing __contains__() Method """
    assert ("A" in LL) == False
    LL.append("A")
    LL.append("B")
    LL.append("C")
    assert ("D" in LL) == False
    LL.append("A")
    LL.append("D")
    LL.append("E")
    assert ("D" in LL) == True
    assert ("A" in LL) == True
    LL.remove("A")
    LL.remove("A")
    assert ("A" in LL) == False

    LL= LinkedList()
    """ Testing __getItem__() Method """
    LL.append("A")
    LL.append("B")
    LL.append("C")
    assert LL[1] == "B"
    assert LL[0] == "A"
    assert LL[2] == "C"
    LL.remove("A")
    assert LL[0] == "B"
    LL.pop(0)
    assert LL[0] == "C"
    assert LL[-1] == "C"

    LL= LinkedList()
    """ Testing __setItem__() Method """
    LL.append("A")
    LL.append("B")
    LL.append("C")
    assert LL[0] == "A"
    LL[0] = "D"
    assert LL[0] == "D"
    LL[0] = "E"
    assert LL[0] == "E"
    LL[-1] = "A"
    assert LL[2] == "A"
    assert LL[-1] == "A"










