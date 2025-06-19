

class Solution:
    def countNumberOfHomogeneousStrings(self, string):
        def combination(num):
            return (num * (num+1)) // 2

        length = len(string); cnt = 0; subStrings = set()
        totalPossibilities = 0
        for pos in range(length):
            if pos != 0 and string[pos] != string[pos-1]:
                # Calculate the possible number of substring combinations
                totalPossibilities  += combination(cnt)
                cnt = 1
            else:
                cnt += 1

        else:
            totalPossibilities += combination(cnt)
                
        return totalPossibilities


obj = Solution()
string = "abbcccaa"

print(obj.countNumberOfHomogeneousStrings(string))