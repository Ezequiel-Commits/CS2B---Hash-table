"""Define a node class for a singly linked list """

class Node:
    def __init__(self, value):
        # What is Proshanto's color scheme? 
        self.value = value
        self.nextNode = None
    
    def __repr__(self):
        return "<" + str(self.value) + ">"

"""Define a linked list class that encapsulates the idea of a linked list """

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, value):
        # O(1) runtime as we don't affect the whole list
        """Push a new node to the head of the list"""
        # 1. Create a new Node object with the given value
        newNode = Node(value)
        # 2. Set the nextNode value of this new node to the previous head value
        newNode.nextNode = self.head
        # 3. Set the head of this linked list to the new node
        self.head = newNode
        return self.head

    def printValues(self):
        # O(n) runtime as the very act of printing all elements takes O(n)
        """print list values(forwards)"""
        # go through all elements and print the values until there is no next node
        currNode = self.head
        # not an empty list
        while currNode != None:
            print(currNode.value)
            # Take your current node and go on to the next node
            currNode = currNode.nextNode
    
    def getNodeByPos(self, position):
        # O(n) runtime as it's required to iterate through all nodes
        """Get a node by position"""
        # Iterate through nodes until you get to a node with the desired "position"
        # Could also be done using a for loop 
        currNode = self.head
        count = 0
        while count < position:
            # print(count, position)
            # Otherwise, keep searching
            count += 1
            currNode = currNode.nextNode
        # you've found the node given a position
        return currNode
    
    def setNodeVal(self, inputValue, position):
        # O(n) runtime as it's required to iterate through nodes
        """set a node value by position"""
        currNode = self.getNodeByPos(position)
        # you've found the node given a position, so set the value
        currNode.value = inputValue
    
    def insertElement(self, nodeBefore, value):
        # O(1) runtime as we don't need to shift values over: instead we do O(1) operations on two nodes
        """Insert element after a given node"""
        # 1. create a new node
        newNode = Node(value)
        # 2. set newNode.nextNode to nodeBefore.nextNode
        newNode.nextNode = nodeBefore.nextNode
        # 3. set nodeBefore.nextNode to newNode
        nodeBefore.nextNode = newNode
    
    def search(self, targetValue):
        # O(n) runtime as we have to iterate through all values in the array
        """Get node by value(i.e. search)"""
        # Go through each element in the list to find a node with the specified value
        currHead = self.head
        while currHead.nextNode != None:
            # There's still nodes to be searched
            if currHead.value == targetValue:
                return str(currHead) + " found"
            currHead = currHead.nextNode
        # One last check on the last node
        if currHead.value == targetValue: #How else could I go about this? 
                return str(currHead) + " found"
        return None
    
    def deleteElement(self, node):
        # O(1) runtime as we only have to interact with two nodes regardless of list size
        """delete element after a given node"""
        # 1. Get a given node's nextNode
        elementToDelete = node.nextNode
        # 2. store the nextNode of the element to delete
        targetNode = elementToDelete.nextNode
        # 2. update the nextNode of the given node to skip a node
        node.nextNode = targetNode
    
    

l = LinkedList()
# n1 = l.push(4)
# n2 = l.push(7)
# n3 = l.push("hello")

# l.setNodeVal("test",0)
# l.insertElement(n3, "test2")

# l.deleteElement(n3)

l.printValues()

# ans = l.search(5)
# print(ans)