class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        for row in grid:
            i = 0
            for num in row:
                if num < 0:
                    res += 1
        return res