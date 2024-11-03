# To find the nearest greater number in a circular array

def nextGreater2(array):
    # Here we will break the array and find the next Greater element
    # For the last element, we will compare with first & others seperately

    length = len(array); pos = length
    answer = [-1]*length; stack = [array[-1]]
    for ele in array[-1::-1]:
        pos -= 1
        val = None
        for e in stack[::-1]:
            if e > ele:
                val = e
                break
        answer[pos] =  val
        if ele > stack[-1]:
            stack[-1] = ele
        else:
            stack.append(ele)
    # Now we will convert the -1's with a number from the left side of array
    for pos in range(length):
        if answer[pos] == None:
            # print(array[pos], stack)
            val = -1
            for e in stack[::-1]:
                if e > array[pos]:
                    val = e
                    break
            answer[pos] = val
    return answer

array = [1,2,1]

res = nextGreater2(array)

print(res)