# To find the next greater element with some constraint

# Methodology
# 1. Construct a sorted array, by adding elements from the reverse side
# 2. For any new element, if the there is any element to its right side then that will be the answer else -1

def nextGreater1(array1, array2):
    # array1 is the subset of array2
    def obtainPosition(ele):
        low, high = 0, len(sorted_array) - 1
        while low <= high:
            mid = (low + high) // 2
            if sorted_array[mid] == ele:
                return mid
            elif sorted_array[mid] < ele:
                low = mid + 1
            else:
                high = mid - 1
        return low

    sorted_array = []; answer = dict()
    print(array2, array1)
    for ele in array2[::-1]:
        pos = obtainPosition(ele)
        print(ele, pos, sorted_array)
        if pos == len(sorted_array):
            answer[ele] = -1
        else:
            answer[ele] = sorted_array[pos]
        sorted_array.insert(pos, ele)
    
    return [answer[i] for i in array1]


nums1 = [4,1,2]
nums2 = [1,3,4,2]

res = nextGreater1(nums1, nums2)

print(res)
