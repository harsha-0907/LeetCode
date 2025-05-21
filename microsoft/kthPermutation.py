
class Solution:
    def kthPermutation(self, arr, k):
        def factorial(n):
            num = 1
            while n > 1:
                num *= n
                n -= 1
            return num
        # For an array of length 'n', to change the first letter it is (n!)+1st attempt
        length = len(arr); arr.sort()
        k = k % (factorial(length)) # To remove the extra iterations

        if k == 0:
            return arr[::-1]
        
        pos = 0; n = length - 1
        while k > 0:
            fact_n = factorial(n)
            quotient = (k-1) // fact_n; k = k % fact_n
            arr.insert(pos, arr.pop(pos+quotient))
            pos += 1; n-= 1
        return arr

obj = Solution()

k = 5
arr = [3, 1, 4, 2]

print(obj.kthPermutation(arr, k))


