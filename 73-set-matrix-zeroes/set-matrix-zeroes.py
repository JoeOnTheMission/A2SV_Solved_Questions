class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        c = set()
        r = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                num = matrix[row][col]
                if num == 0:
                    if row not in r:
                        r.add(row)
                    if col not in c:
                        c.add(col)
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row in r or col in c:
                    matrix[row][col] = 0