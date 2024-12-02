# Create a Stack using Linked List

class MyQueue:
    def __init__(self):
        self.rear = None
        self.front = None


        
    def push(self, data): 
        temp = Node(data)
        if self.front == None:
            self.front = temp
            self.rear = temp
        else:
            self.rear.next = temp
            self.rear = temp

 

    def pop(self):
        if self.front is None:
            return -1
        else:
            res= self.front.data
            self.front = self.front.next
            if self.front== None:
                self.rear==None
            return res
    def __init__(self):
        self.top = None
        
    def push(self, data):
        newnode = StackNode(data)
        if self.top:
            self.top.next = newnode
            self.top = newnode
        else:
            self.top = newnode
    
    def pop(self):
        if self.top