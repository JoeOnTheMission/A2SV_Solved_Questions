class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    box[i//3,j//3].add(board[i][j])

        def solver(i,j):
            if i > 8:
                return True
            if board[i][j] != ".":
                if j < 8:
                    return solver(i, j+1)
                else:
                    return solver(i+1, 0)
                
            valids = []
            for x in range(1,10):
                num = str(x)
                if num in row[i] or num in col[j] or num in box[i//3,j//3]:
                    continue

                # add to board
                board[i][j] = num
                row[i].add(num)
                col[j].add(num)
                box[i//3,j//3].add(num)
                #print(num)

                if j < 8:
                    if solver(i, j+1):
                        return True
                else:
                    if solver(i+1, 0):
                        return True
                board[i][j] = "."
                row[i].remove(num)
                col[j].remove(num)
                box[(i//3, j//3)].remove(num)            
            return False
        solver(0,0)