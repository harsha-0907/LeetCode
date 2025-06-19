

class Solution:
    def sortCharacters(self, string):
        dict1 = {}
        for ch in string:
            if ch in dict1:
                dict1[ch] += 1
            else:
                dict1[ch] = 1
        sortedKeys = sorted(dict1, key=lambda x: dict1[x], reverse=True)
        newList = [ch for ch in sortedKeys for i in range(dict1[ch])] 
        # print(newList)
        return ''.join(newList)


obj = Solution()

string = "aaacc"

print(obj.sortCharacters(string))