class Solution:
    def initializeHeap(self):
        self.minHeap = []
        return None

    def insert(self, key):
        # Insert the key first
        self.minHeap.append(key)
        child = len(self.minHeap)-1; parent = (child-1) // 2
        
        while child > 0:
            if self.minHeap[parent] <= self.minHeap[child]:
                break
            self.minHeap[parent], self.minHeap[child] = self.minHeap[child], self.minHeap[parent]
            parent, child = parent // 2, child // 2
        

    def changeKey(self, index, new_val):
        old_val = self.minHeap[index]
        self.minHeap[index] = new_val

        if new_val < old_val:
            # Percolate up
            child = index
            parent = (child - 1) // 2
            while child > 0 and self.minHeap[child] < self.minHeap[parent]:
                self.minHeap[child], self.minHeap[parent] = self.minHeap[parent], self.minHeap[child]
                child = parent
                parent = (child - 1) // 2
        else:
            # Percolate down
            parent = index
            length = len(self.minHeap)
            while True:
                left = 2 * parent + 1
                right = 2 * parent + 2
                smallest = parent

                if left < length and self.minHeap[left] < self.minHeap[smallest]:
                    smallest = left
                if right < length and self.minHeap[right] < self.minHeap[smallest]:
                    smallest = right

                if smallest == parent:
                    break

                self.minHeap[parent], self.minHeap[smallest] = self.minHeap[smallest], self.minHeap[parent]
                parent = smallest

    def extractMin(self):
        if not self.minHeap:
            return None  # Or raise an exception if preferred

        self.minHeap[0], self.minHeap[-1] = self.minHeap[-1], self.minHeap[0]
        min_val = self.minHeap.pop()  # Remove the last element (original min)

        parent = 0
        length = len(self.minHeap)

        while True:
            left = 2 * parent + 1
            right = 2 * parent + 2
            smallest = parent

            if left < length and self.minHeap[left] < self.minHeap[smallest]:
                smallest = left
            if right < length and self.minHeap[right] < self.minHeap[smallest]:
                smallest = right

            if smallest == parent:
                break

            self.minHeap[parent], self.minHeap[smallest] = self.minHeap[smallest], self.minHeap[parent]
            parent = smallest



    def isEmpty(self):
        return True if len(self.minHeap) == 0 else False
    def getMin(self):
        return self.minHeap[0]

    def heapSize(self):
        return len(self.minHeap)
