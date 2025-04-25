# Converting the minheap to maxheap

class Solution:
    def heapify(self, parent, N, nums):
        child_a_pos, child_b_pos = (parent*2) + 1, (parent*2) + 2
        
        new_pos = parent
        if child_a_pos < N and nums[parent] < nums[child_a_pos]:
            new_pos = child_a_pos
        if child_b_pos < N and nums[new_pos] < nums[child_b_pos]:
            new_pos = child_b_pos
        
        if new_pos != parent:
            # Heapify the child
            nums[parent], nums[new_pos] = nums[new_pos], nums[parent]
            self.heapify(new_pos, N, nums)

    def minToMaxHeap(self, nums):
        N = len(nums)
        for parent in range(int((N-2)/2), -1, -1):
            # print(parent)
            self.heapify(parent, N, nums)