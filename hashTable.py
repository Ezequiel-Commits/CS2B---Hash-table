"""Implementation of a hash table: similar to a dictionary"""
import linkedList
import hashFunction
import random


class HashTable:
    def __init__(self, nOfBuckets):
        # Create data structure to make look up by value O(1) on average
        self.HashTable = []
        self.nOfBuckets = nOfBuckets
        # select a random hashFunction from the hashFunctionLibrary
        function = hashFunction.hashFunction()
        hashFunctions = [function.executeFunction1, function.executeFunction2, function.executeFunction3]
        randomIndex = random.randint(0, 2)
        self.hashFunction = hashFunctions[randomIndex]
    
    def createTable(self):
        # Create a hash table with nOfBuckets' elements
        for bucket in range(self.nOfBuckets):
            self.HashTable.append(linkedList.LinkedList())
    
    def __repr__(self):
        index = 0
        for linkedList in self.HashTable:
            # print the values of each linkedList in the hash table and set each bucket of the hashtable to that ans
            ans = linkedList.printValues()
            self.HashTable[index] = ans #Not sure why an extra none is printed at the end of some indices.
            print(self.HashTable[index])
            index += 1
        return

    def addToBucket(self, value, bucket):
        # 1. Get the linkedList associated with the bucket
        targetLinkedList = self.HashTable[bucket]
        # 2. add a node to that linkedList with the given value
        targetLinkedList.push(value)
        pass

    def addToTable(self, value):
        # 1. execute the hashFunction to get the bucket 
        bucket = self.hashFunction(value = value, nOfBuckets = self.nOfBuckets) 
        print(value, bucket)
        # 2. add an element to the associated bucket using the pre-defined method
        self.addToBucket(value = value, bucket = bucket)
    
    def search(self, value):
        """Search for an element by value in O(1) time"""
        # 1. Get the bucket of the value using the hashFunction
        bucket = self.hashFunction(value = value, nOfBuckets = self.nOfBuckets) 
        # 2. use the search method of the linked list to go through each node in the bucket
        return self.HashTable[bucket].search(targetValue = value)

hashFunction1 = hashFunction.hashFunction()

# Create an object of class HashTable
myHashTable = HashTable(nOfBuckets = 10)
# Fill the object(currently an empty array) with buckets(empty linkedLists)
myHashTable.createTable()
# Add values to the table
myHashTable.addToTable(19)
myHashTable.addToTable(22)
myHashTable.addToTable(9)
myHashTable.addToTable(12)
myHashTable.addToTable(23)
myHashTable.addToTable(5)
# Example of an error through using different hash functions. 
ans = myHashTable.search(9)
print(ans)
ans = myHashTable.search(22)
print(ans)
ans = myHashTable.search(19)
print(ans)
# myHashTable.__repr__()