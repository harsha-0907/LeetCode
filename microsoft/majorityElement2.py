

class Solution:
    def majorityElement2Brute(self, arr):
        dict1 = {}
        for ele in arr:
            if ele in dict1:
                dict1[ele] += 1
            else:
                dict1[ele] = 1
        length = len(arr); maxEle = []
        for ele in dict1:
            if dict1[ele] > length // 3:
                maxEle.append(ele)
        return maxEle

    def majorityElement2(self, arr):
        ele1 = ele2 = ele3 = None
        e1 = e2 = e3 = 0
        for ele in arr:
            if ele1 and ele2 and ele3:
                break
            if ele1 is None:
                ele1 = ele
            elif ele == ele1:
                pass
            elif ele2 is None:
                ele2 = ele
            elif ele == ele2:
                pass
            elif ele3 is None:
                ele3 = ele
                break
        
        for ele in arr:
            if ele == ele1:
                e1 += 1
            elif ele == ele2:
                e2 += 1
            elif ele == ele3:
                e3 += 1
            

            
        pass
obj = Solution()
arr = [3, 2, 1]

print(obj.majorityElement2(arr))