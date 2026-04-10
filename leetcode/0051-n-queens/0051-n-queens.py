class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiag = set() # r+c
        negDiag = set() # r-c
        cur = []
        res = []
        def genrator(index):
            len(cur) - index
        
        def backtrack(cur):
            if len(cur) == n:
                res.append(cur[:])
            for j in range(n):
                
                pos = len(cur) + j
                neg = len(cur) - j
                if pos not in posDiag and neg not in negDiag and j not in cols:
                    cols.add(j)
                    posDiag.add(pos)
                    negDiag.add(neg)
                    row ="".join(["." if i != j else "Q" for i in range(n)])
                    

                    cur.append(row)
                    backtrack(cur)
                    cur.pop()

                    cols.remove(j)
                    posDiag.remove(pos)
                    negDiag.remove(neg)
        backtrack([])
        return res

