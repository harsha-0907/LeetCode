

class Solution:
    def pascalTriangle(self, k):
        triangleRows = [[1], [1,1]]
        for i in range(2, k):
            parentRow = triangleRows[i-1]; length = len(parentRow)
            newRow = [1]
            for j in range(length):
                topEle = parentRow[j+1] if j + 1 < length else 0
                tot = parentRow[j] + topEle
                newRow.append(tot)

            triangleRows.append(newRow)

        return triangleRows
    
    def pascalTriangleThought(self, k):
        pascalTriangle = [1]
        for i in range(1, k):
            newRow = pascalTriangle[i-1] * 11
            pascalTriangle.append(i)
        
        return pascalTriangle

        
obj = Solution()
print(obj.pascalTriangle(4))
