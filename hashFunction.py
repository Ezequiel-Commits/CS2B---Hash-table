"""Implementation of functions to be used in a hash table"""

class hashFunction:
    # The concept of a function for a hash table

    def __init__(self):
        pass

    def executeFunction1(self, value, nOfBuckets):
        # Division method
        return value % nOfBuckets
    
    def executeFunction2(self, value, nOfBuckets):
        # Multiplication method
        constant = .357 
        return int(nOfBuckets * (value * constant % 1))
    
    def executeFunction3(self, value, nOfBuckets):
        # An attempt of the Mid Square Method
        Square = value * value
        bucket = Square % nOfBuckets
        return bucket