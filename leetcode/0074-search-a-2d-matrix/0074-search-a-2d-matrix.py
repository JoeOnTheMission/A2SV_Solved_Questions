class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        left = 0
        right = n * m - 1
        while left <= right:
            mid = left + (right - left)//2
            #print("1st",n,m)
            #print("2nd",left,mid,right)
            #print("3rd",mid,mid//2,mid%2)
            if matrix[mid // m][mid % m] < target:
                left = mid + 1
            else:
                right = mid - 1
        i = left // m
        j = left % m
        #print(n,m)
        #print(i,j)

        if i < n and j < m and matrix[i][j] == target:
            return True
        return False
