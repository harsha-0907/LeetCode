# Merge k sorted lists
import heapq
class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for list_ele in lists:
            while list_ele is not None:
                ele = list_ele.val
                heapq.heappush(arr, ele)
                list_ele = list_ele.next
        
        headNode = ListNode(); parent = headNode
        while len(arr) > 0:
            ele = heapq.heappop(arr)
            newNode = ListNode(ele)
            parent.next = newNode
            parent = newNode
        
        return headNode.next
    
    def mergeKListsInOofN(self, lists: List[Optional[ListNode]]) ->  Optional[ListNode]:
        headNode = ListNode(); parent = headNode
        kHeap = []
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(kHeap, (head.val, i))
                lists[i] = lists[i].next

        while len(kHeap) > 0:
            val, list_index = heapq.heappop(kHeap)
            newNode = ListNode(val)
            parent.next = newNode
            parent = newNode

            if lists[list_index] is not None:
                ele = (lists[list_index].val, list_index)
                lists[list_index] = lists[list_index].next
                heapq.heappush(kHeap, ele)

        return headNode.next