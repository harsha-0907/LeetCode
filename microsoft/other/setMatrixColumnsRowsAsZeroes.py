
class Solution:
    def setMatrixColumnsRowsAsZeroes(self, matrix):
        row, col = len(matrix), len(matrix[0])
        isZeroRow, isZeroColumn = False, False

        for i in range(row):
            if matrix[i][0] == 0:
                isZeroColumn = True
                break

        for i in range(col):
            if matrix[0][i] == 0:
                isZeroRow = True
                break
        
        print(isZeroRow, isZeroColumn)
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
            
        for i in range(1, row):
            if matrix[i][0] == 0:
                for j in range(1, col):
                    matrix[i][j] = 0
        
        for j in range(1, col):
            if matrix[0][j] == 0:
                for i in range(1, row):
                    matrix[i][j] = 0
        
        if isZeroColumn:
            for i in range(row):
                matrix[i][0] = 0

        if isZeroRow:
            for j in range(col):
                matrix[0][j] = 0

        return matrix

obj = Solution()
arr = [[0,2,3], [3,0,1], [2,1,3]]
print(arr)
print(obj.setMatrixColumnsRowsAsZeroes(arr))