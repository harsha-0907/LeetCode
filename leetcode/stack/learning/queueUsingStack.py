# Create a Stack using Queue

class MyQueue:
    def __init__(self):
        self.stack = []
        self.temp = []

    def push(self, x: int) -> None:
        # Insertion at the end
        self.stack.append(x)

    def pop(self) -> int:
        if self.empty():
            return True
        else:
            self.temp = []
            for ele in self.stack[::-1]:
                self.temp.append(ele)
            
            for ele in self.temp[-2::-1]:
                self.stack.append(ele)
            return self.temp.pop()

    def peek(self) -> int:
        if self.empty():
            return -1
        return self.stack[0]

    def empty(self) -> bool:
        if self.stack == []:
            return True
        return False
