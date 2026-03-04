class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        #identify valid rows
        valid_rows = set()
        for i in range(len(mat)):#row
            if sum(mat[i]) == 1:
                valid_rows.add(i)
        col = [0]*len(mat[0])
        #identify valid cols and indexes which have 1
        check = []
        for i in range(len(mat)):#  
            for j in range(len(mat[0])):
                col[j] += mat[i][j]
                if mat[i][j] == 1:
                    check.append([i,j])
        valid_cols = set()
        for i,value in enumerate(col):
            if value == 1:
                valid_cols.add(i)
        
        res = 0    
        for row , col in check:
            if row in valid_rows and col in valid_cols:
                res += 1
        return res