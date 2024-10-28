# The shortest palindrome possible with the given string

def shortestPalindrome(string):
    def oddPalindrome(mid):
        i = 0
        while mid - i >= 0:
            if string[mid-i] == string[mid+i]:
                pass
            else:
                return n
            i += 1
        if mid + i != n:
            return n - mid - i
        return 0
    
    def evenPalindrome(start, end):
        i = 0
        while start - i >= 0:
            if string[start-i] != string[end + i]:
                return n
            i += 1
        
        if end + i != n:
            return (n-end-i)

        return 0

    n = len(string); mid = (n-1) // 2
    minlen = 100000
    for i in range(mid, -1, -1):
        minlen = min(minlen, oddPalindrome(i))
        if i > 0:
            #print(i-1, i)
            minlen = min(minlen, evenPalindrome(i-1, i))

    return string[-1:-minlen-1:-1] + string

def isPalindrome(string):
    s1 = string[-1::-1]
    if s1 == string:
        return True
    else:
        return False
string = "abcd"
res = shortestPalindrome(string)
print(res, isPalindrome(res))