

class Solution:
    def kDistinctSubstringsBrute(self, string, k):
        # Find all the substrings and count the number of substrings that satisfy the condition
        subStrings = []; length = len(string)
        for i in range(1, length+1):
            for j in range(length-i+1):
                s = string[j:j+i]
                # print(s, j, j+i)
                if len(set(s)) == k:
                    subStrings.append(s)


        return len(subStrings)

    def countAtMostK(self, s, k):
        from collections import defaultdict
        count = 0
        left = 0
        freq = defaultdict(int)
        unique = 0

        for right in range(len(s)):
            if freq[s[right]] == 0:
                unique += 1
            freq[s[right]] += 1

            while unique > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    unique -= 1
                left += 1

            count += right - left + 1
        return count

    def kDistinctSubstrings(self, string, k):
        return self.countAtMostK(string, k) - self.countAtMostK(string, k - 1)

obj = Solution()
string = "uvgugewmed"
k = 3

print(obj.kDistinctSubstrings(string, k))