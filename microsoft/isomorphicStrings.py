
class Solution:
    def isomorphicString(self, string1: str, string2: str):
        replacmentDict = {}; length = len(string1)
        if length != len(string2):
            return False
        for pos in range(length):
            ch1 = string1[pos]; ch2 = string2[pos]
            if ch1 in replacmentDict:
                if replacmentDict[ch1] != ch2:
                    return False
            else:
                if ch2 in replacmentDict.values():
                    return False
                replacmentDict[ch1] = ch2
            
        return True

obj = Solution()

string1 = "egg"
string2 = "add"

print(obj.isomorphicString(string1, string2))