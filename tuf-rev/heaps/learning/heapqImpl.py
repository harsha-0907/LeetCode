

class Heap:
    def __init__(self):
        self.minHeap = []
    
    def push(self, ele):
        self.minHeap.append(ele)
        child_pos = len(self.minHeap) - 1; parent_pos = (child_pos - 1) // 2
        while self.minHeap[parent_pos] > self.minHeap[child_pos] and parent_pos >= 0:
            self.minHeap[parent_pos], self.minHeap[child_pos] = self.minHeap[child_pos], self.minHeap[parent_pos]
            child_pos, parent_pos = parent_pos, (parent_pos-1) // 2

    def pop(self):
        self.minHeap[0], self.minHeap[-1] = self.minHeap[-1], self.minHeap[0]
        removed_ele = self.minHeap.pop()
        parent_pos = 0; length = len(self.minHeap)
        while parent_pos < length:
            child_a_pos, child_b_pos = (parent_pos*2)+1, (parent_pos*2)+2
            newparent = parent_pos
            if child_a_pos < length and self.minHeap[newparent] > self.minHeap[child_a_pos]:
                newparent = child_a_pos
            if child_b_pos < length and self.minHeap[newparent] > self.minHeap[child_b_pos]:
                newparent = child_b_pos
            
            if newparent == parent_pos:
                break
            else:
                self.minHeap[newparent], self.minHeap[parent_pos] = self.minHeap[parent_pos], self.minHeap[newparent]
                parent_pos = newparent
        
        return removed_ele

    def heapify(self):
        n = (len(self.minHeap)//2) - 1
        for i in range(n, -1, -1):
            self.heapifyPosition(i)
    
    def heapifyPosition(self, i):
        length = len(self.minHeap)
        child_pos_a, child_pos_b = (i*2)+1, (i*2)+2
        newi = i

        if child_pos_a < length and self.minHeap[child_pos_a] < self.minHeap[newi]:
            newi = child_pos_a
        if child_pos_b < length and self.minHeap[child_pos_b] < self.minHeap[newi]:
            newi = child_pos_b

        if newi != i:
            self.minHeap[newi], self.minHeap[i] = self.minHeap[i], self.minHeap[newi]
            self.heapifyPosition(newi)

    def minElement(self):
        if len(self.minHeap) > 0:
            return self.minHeap[0]
        return None

h = Heap()
for num in [9, 4, 7, 1, 2, 6]:
    h.push(num)

print("Min element:", h.minElement())  # ➜ 1
print("Popped:", h.pop())              # ➜ 1
print("New Min:", h.minElement())      # ➜ 2
print("Heap:", h.minHeap)              # Should maintain min-heap property
