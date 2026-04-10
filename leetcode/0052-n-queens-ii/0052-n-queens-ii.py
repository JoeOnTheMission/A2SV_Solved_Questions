class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        posDiag = set() # r+c
        negDiag = set() # r-c
        cur = []
        self.res = 0
        
        def backtrack(cur):
            if len(cur) == n:
                self.res += 1
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
        return self.res