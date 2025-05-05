
class Solution:    
    def minimumPlatform(self,arr,dep):
        length = len(arr)
        timings = {arr[i]: dep[i] for i in range(length)}
        arr.sort(); dep.sort()
        max_platforms = platform_cnt = 0
        arr_pos = dep_pos = 0

        while dep_pos < length:
            if arr_pos < length and arr[arr_pos] <= dep[dep_pos]:
                platform_cnt += 1
                # print("Train Comes: ", arr[arr_pos], " - ", platform_cnt)
                arr_pos += 1
            else:
                platform_cnt -= 1
                # print("Train Goes: ", arr[dep_pos], " - ", platform_cnt)
                dep_pos += 1
            max_platforms = max(max_platforms ,platform_cnt)
            # print(platform_cnt, max_platforms)
        
        return max_platforms


arr = "900 940 950 1100 1500 1800"
dep = "910 1200 1120 1130 1900 2000"
arr = [int(i) for i in arr.split()]; dep = [int(i) for i in dep.split()]
obj = Solution()
print(obj.minimumPlatform(arr, dep))