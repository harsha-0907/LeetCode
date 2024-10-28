# To find the kth binary bit in the nth binary bit

# Optimized Brute-force
def findKthBit(n: int, k: int) -> str:
    def Si(Si_1):
        def Invert(string):
            ans = ""
            for i in string:
                if i == '0':
                    ans += '1'
                else:
                    ans += '0'
            
            return ans
        Si_1 = Si_1 + '1' + Invert(Si_1[-1::-1])
        return Si_1
    s1 = '0'
    for i in range(n):
        if len(s1) >= k:
            return s1[k-1]
        s1 = Si(s1)

    return s1[k-1]

def findKthBit1(n: int, k: int) -> str:
    length = 2 ** (n) - 1
    mid = length // 2
    
    if k == mid:
        return `1`

    elif k < mid:
        return findKthBit1(n-1, k)
    else:
        return '1' if findKthBit1(n - 1, length - k + 1) == '0' else '0'
    
n = 4
k = 11

res = findKthBit(n, k)

print(res)