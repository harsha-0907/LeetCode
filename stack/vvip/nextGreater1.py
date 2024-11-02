# To find the element that is immediately greater to the given number

# Procedure:
# 1. Use a stack to store all the elements that are actually less than the element while traversing reverse
# 2. Print all the elements at last

def nextGreater(array1, array2):
    # array1 is a subset of array2
    answer = {array2[-1]: -1}; stack = [array2[-1]]
    for ele in array2[-2::-1]:
        if ele in array1:
            maxele = -1
            for maxi in stack[::-1]:
                if maxi > ele:
                    maxele = maxi
                    break
            answer[ele] = maxele
        if ele > stack[-1]:
            stack[-1] = ele
        else:
            stack.append(ele)
    return [answer[i] for i in array1]
        

nums1 = [4,1,2]
nums2 = [1,3,4,2]

res = nextGreater(nums1, nums2)

print(res)