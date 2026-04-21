class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        n = len(board)
        m = len(board[0])
   
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        def capture(i, j):
            if not (0 <= i < n and 0 <= j < m):
                return False

            if board[i][j] == "X":
                return True

            if board[i][j] == "T":
                return True  
                
            board[i][j] = "T"

            up = capture(i-1, j)
            down = capture(i+1, j)
            left = capture(i, j-1)
            right = capture(i, j+1)

            return up and down and left and right

        def marker(i,j,mark):
            if not (0 <= i < n and 0 <= j < m) or board[i][j] != "T":
                return

            board[i][j] = mark

            for i_change,j_change in direction:
                new_i = i + i_change
                new_j = j + j_change
                marker(new_i,new_j,mark)



        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    surrounded = capture(i,j)
                    if surrounded:#change to X
                        marker(i,j,"X")

        for i in range(n):
            for j in range(m):
                if board[i][j] == "T":
                    board[i][j] = "O"
    