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

