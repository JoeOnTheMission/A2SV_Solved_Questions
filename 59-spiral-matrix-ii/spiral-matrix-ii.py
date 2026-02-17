class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for row in range(n)]

        right = True
        down = False
        left = False
        up = False
        i = 0 
        j = 0
        wall = {"r" : len(matrix[0]),"d" : len(matrix),"l" : -1,"u" : -1}
        now = 1
        while wall["u"] < i < wall["d"] and wall["l"] < j < wall["r"]:
            
            if right:
                while j < wall["r"]:
                    matrix[i][j] = now
                    now += 1
                    j += 1
                wall["u"] = i
                j -= 1# fix while loop 
                i += 1# go to next element 
                right = not(right)
                down = not(down)
                
            if down:
                while i < wall["d"]:
                    matrix[i][j] = now
                    now += 1
                    i += 1
                wall["r"] = j
                i -= 1# fix while loop
                j -= 1# go to next
                down = not(down)
                left = not(left)
                
            if left:
                while j > wall["l"]:
                    matrix[i][j] = now
                    now += 1
                    j -= 1
                wall["d"] = i
                j += 1#fix while loop
                i -= 1#go to next
                left = not(left)
                up = not(up)
                
            if up:
                while i > wall["u"]:
                    matrix[i][j] = now
                    now += 1
                    i -= 1
                wall["l"] = j
                i += 1 #fix while loop
                j += 1 #go to the next 
                up = not(up)
                right = not(right)
            
        return matrix
            