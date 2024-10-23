# To implement a min stack
class MinStack:
    def binSearch(self, ele):
        low = 0; high = len(self.heap)-1
        while low <= high:
            mid = (low + high) // 2
            if self.heap[mid] == ele:
                return mid
            elif self.heap[mid] < ele:
                low = mid + 1
            else:
                high = mid - 1
        return low
        
    def __init__(self):
        self.array = []
        self.heap = []

    def push(self, ele: int) -> None:
        self.array.append(ele)
        pos = self.binSearch(ele)
        self.heap.insert(pos, ele)
        #print(self.heap)

    def pop(self) -> None:
        ele = self.array.pop()
        pos = self.binSearch(ele)
        self.heap.remove(self.heap[pos])

    def top(self) -> int:
        if self.array == []:
            return -1
        return self.array[-1]

    def getMin(self) -> int:
        return self.heap[0]

