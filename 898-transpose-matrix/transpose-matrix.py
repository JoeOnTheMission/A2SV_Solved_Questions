class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new_matrix = []
        y = 0
        x = 0
        for x in range(len(matrix[0])):
            new_row = []
            for y in range(len(matrix)):
                new_row.append(matrix[y][x])
            new_matrix.append(new_row)
        return new_matrix