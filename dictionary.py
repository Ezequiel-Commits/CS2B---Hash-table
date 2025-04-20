"""Implementation of a hash table: similar to a dictionary"""
import linkedList


class HashTable:
    def __init__(self, nOfBuckets):
        # Create data structure to make look up by value O(1) on average
        self.HashTable = []
        self.nOfBuckets = nOfBuckets
    
    def createTable(self):
        # Create a hash table with nOfBuckets' elements
        for bucket in range(self.nOfBuckets):
            # Add a linked list for each bucket
            self.HashTable.append(linkedList.LinkedList())
    
    def __repr__(self):
        index = 0
        for aList in self.HashTable:
            # print the values of each linkedList in the hash table and set each bucket of the hashtable to that ans
            ans = aList.printValues()
            self.HashTable[index] = ans
            index += 1
        return str(self.HashTable)

    def addToBucket(self, value, bucket):
        # 1. Get the linkedList associated with the bucket
        print(value, bucket)
        targetLinkedList = self.HashTable[bucket]
        # 2. add a node to that linkedList with the given value
        targetLinkedList.push(value)
        targetLinkedList.printValues()
        pass

    def addToTable(self, value):
        # 1. define a hashFunction
        bucket = value % self.nOfBuckets #Not sure "key" is the right term
        print(bucket)
        # 3. add an element to the associated bucket using the pre-defined method
        self.addToBucket(value = value, bucket = bucket)
    
    def search(self, value):
        pass

myHashTable = HashTable(nOfBuckets = 10)
myHashTable.createTable()
myHashTable.addToTable(12)
print(myHashTable)
# myHashTable.add(5, 10)