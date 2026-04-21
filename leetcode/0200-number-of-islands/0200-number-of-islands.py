class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        def inbound(row,col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        def dfs(r,c):
            if not inbound(r,c) or grid[r][c] == "0":
                return 

            #update to say visited
            grid[r][c] = "0"

            for row_update,col_update in direction:
                a = r + row_update
                b = c + col_update
                dfs(a,b)
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i,j)
                    res += 1
        return res