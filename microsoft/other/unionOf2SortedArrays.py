

class Solution:
    def unionOf2SortedArrays(self, arr1, arr2):
        newarray = []; length1, length2 = len(arr1), len(arr2)
        i, j = 0, 0
        while i < length1 or j < length2:
            ele1 = arr1[i] if i < length1 else float('inf')
            ele2 = arr2[j] if j < length2 else float('inf')
            if ele1 <= ele2:
                i += 1
                ele = ele1
            else:
                j += 1
                ele = ele2
            if newarray == []:
                newarray.append(ele)
            elif newarray[-1] != ele:
                newarray.append(ele)
    
        return newarray

obj = Solution()
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]

print(obj.unionOf2SortedArrays(arr1, arr2))