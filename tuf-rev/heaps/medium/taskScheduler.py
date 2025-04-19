
class Solution:
    def taskSchedulerApproach1(self, arr, n):
        length = len(arr); arr = sorted(arr)
        positions = []
        dict1 = dict(); front_pos = 0
        completed_pos = []
        for ch in arr:
            if ch in dict1:
                dict1[ch] += n + 1
                positions.append((dict1[ch], ch))
                completed_pos.append(dict1[ch])
            else:
                if front_pos in completed_pos:
                    while front_pos in completed_pos:
                        front_pos += 1
                dict1[ch] = front_pos
                completed_pos.append(dict1[ch])
                positions.append((dict1[ch], ch))
                front_pos += 1
        maxi = 0; print(dict1)
        print(sorted(positions))
        for i in dict1:
            maxi = max(maxi, dict1[i])
        return maxi + 1
    
    def taskSchedulerApproach2(self, arr, n):
        dict1 = dict(); fmax = 0
        for ele in arr:
            if ele in dict1:
                dict1[ele] += 1
            else:
                dict1[ele] = 1
            fmax = max(fmax, dict1[ele])
        
        x = 0
        for ele in dict1:
            if dict1[ele] == fmax:
                x += 1
        
        return max(((n+1)*(fmax-1)+x), len(arr))
        
                


arr = ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"]
n = 2
# A, B, C, A, B, C, A, B, C, D, E, idle, D

ob = Solution()

print(ob.taskSchedulerApproach2(arr, n))