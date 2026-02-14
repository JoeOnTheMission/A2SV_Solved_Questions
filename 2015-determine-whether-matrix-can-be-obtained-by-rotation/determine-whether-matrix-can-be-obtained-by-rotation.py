class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        for _ in range(3):
            n = len(mat)
            for i in range(n):
                for j in range(i+1,n):
                    mat[i][j],mat[j][i] = mat[j][i], mat[i][j]
            for row in mat:
                row.reverse()
            if mat == target:
                return True
        else:
            return False