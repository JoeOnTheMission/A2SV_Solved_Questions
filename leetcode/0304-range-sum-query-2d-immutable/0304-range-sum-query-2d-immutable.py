class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        self.pre = [[0]*(len(matrix[0])+1) for i in range(len(matrix)+1)]
        
        for i in range(1,len(matrix)+1):
            for j in range(1,len(matrix[0])+1):
                self.pre[i][j] = self.pre[i-1][j] + self.pre[i][j-1] - self.pre[i-1][j-1] + matrix[i-1][j-1]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1
       
        self.sub_sum = self.pre[row2][col2] - self.pre[row2][col1 - 1] - self.pre[row1 - 1][col2 ] + self.pre[row1 - 1][col1 - 1]
        return self.sub_sum
"""        
# Your NumMatrix object will be instantiated and called as such:
matrix  = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
obj = NumMatrix(matrix)
param_1 = obj.sumRegion(2,2,4,4)
print(param_1)"""