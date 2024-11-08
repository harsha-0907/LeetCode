# To find the next nearest element that is before this number(Interview Bit)

def nextSmaller(array):
    length = len(array); pos = 1
    stack = [array[0]]; answer = [-1] * length
    for ele in array[1:]:
        val = -1
        for e in stack[::-1]:
            if e < ele:
                val = e
                break
        answer[pos] = val
        if ele < stack[-1]:
            stack[-1] = ele
        else:
            stack.append(ele)
        pos += 1
    return answer

array = [4, 5, 2, 10, 8]

res = nextSmaller(array)

print(res)
