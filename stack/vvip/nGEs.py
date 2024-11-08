# To find the count of the number of elements greater than the ele to its right

# Brute-force always works
def nGEBrute(array1, indices):
    # Time - O(n**2)
    length = len(array1); pos1 = -1
    answer = [0] * len(indices)
    for index in indices:
        cnt = 0; pos1 += 1
        for pos in range(index, length):
            if array1[pos] > array1[index]:
                cnt += 1
        answer[pos1] = cnt
    return answer

def nGEs(array, indices):
    answer = []
    for index in indices:
        cnt = 0
        for pos in range(index+1, N):
            if array[pos] > array[index]:
                cnt += 1
        answer.append(cnt)
    # print(answer)
    return answer

array1 = [3, 4, 2, 7, 5, 8, 10, 6]
array2 = [0, 5]

res = nGEs(array1, array2)

print(res)