import heapq

# https://leetcode.com/problems/hand-of-straights/

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        length = len(hand)
        if length % groupSize:
            return False
        dict1 = dict()
        for ele in hand:
            if ele in dict1:
                dict1[ele] += 1
            else:
                dict1[ele] = 1
        if len(dict1) < groupSize:
            return False
        keys = sorted(dict1.keys())
        while keys != []:
            if len(keys) < groupSize:
                return False
            parent, child = None, None
            for i in range(groupSize):
                child = keys[i]
                if parent is None:
                    parent = child
                elif child - parent == 1:
                    parent = child
                else:
                    return False
                if dict1[child] == 1:
                    dict1.remove(child)
                else:
                    dict1[child] -= 1
        
            keys = sorted(dict1.keys())
        
        return True

    def isNStraightHandOptimal(self, hand: List[int], groupSize: int) -> bool:
        pass