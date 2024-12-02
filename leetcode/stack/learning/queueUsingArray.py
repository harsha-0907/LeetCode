# Implementing queue using an array

class MyQueue:
    
    def __init__(self):
        self.arr = []
    
    #Function to push an element x in a queue.
    def push(self, x):
        self.arr.insert(0, x)        
        
    #Function to pop an element from queue and return that element.
    def pop(self): 
        if self.arr == []:
            return -1
        else:
            self.arr.pop()