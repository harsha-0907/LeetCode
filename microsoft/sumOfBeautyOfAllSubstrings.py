

class Solution:
    def maxMinFreq(self, freqs: dict):
        values = freqs.values()
        return max(values), min(values)

    def sumOfBeautyOfAllSubstrings(self, string):
        # Brute Force Approach
        length = len(string); totalBeauty = 0
        # We consider substrings of size 1 to length
        for i in range(2, length+1):
            freq = {}
            for j in range(i):
                ch = string[j]
                if ch in freq:
                    freq[ch] += 1
                else:
                    freq[ch] = 1
            maxFreq, minFreq = self.maxMinFreq(freq)
            totalBeauty += maxFreq - minFreq

            for j in range(length-i):
                freq[string[j]] -= 1
                if freq[string[j]] == 0:
                    del(freq[string[j]])

                ch = string[j+i]
                if ch not in freq:
                    freq[ch] = 1
                else:
                    freq[ch] += 1
                maxF, minF = self.maxMinFreq(freq)
                totalBeauty += maxF - minF

        return totalBeauty


obj = Solution()
string = "aabcbaa"

print(obj.sumOfBeautyOfAllSubstrings(string))