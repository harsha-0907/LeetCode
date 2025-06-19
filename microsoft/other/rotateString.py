

class Solution:
    def rotateString(self, string1, string2):
        # Lets rotate the string2
        if len(string1) != len(string2):
            return False
        if string1 == string2:
            return True

        length = len(string2)
        for i in range(length-1):
            string2 = string2[1:] + string2[0]
            if string1 == string2:
                return True
                
        return False

obj = Solution()

string1 = "abcde"
string2 = "cdeab"

print(obj.rotateString(string1, string2))