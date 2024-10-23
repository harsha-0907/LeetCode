# Implementing Stack using queues

class MyStack:
    def __init__(self):
        self.queue1 = []
        self.temp = []
        
    def push(self, x: int) -> None:
        self.queue1.append(x)
        # Adding element at the last

    def pop(self) -> int:
        if self.empty():
            return -1
        else:
            self.temp = []
            # 1 2 3
            for ele in self.queue1[::-1]:
                self.temp.append(ele)
            self.queue1 = []
            # 3 2 1
            for ele in self.temp[1:]:
                self.queue1.insert(0, ele)
            return self.temp[0]

    def top(self) -> int:
        if self.empty():
            return -1
        else:
            return self.queue1[-1]
        
    def empty(self) -> bool:
        # print(self.queue1)
        if self.queue1 == []:
            return True
        return False
