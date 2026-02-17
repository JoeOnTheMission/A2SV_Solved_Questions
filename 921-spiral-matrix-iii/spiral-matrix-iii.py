class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        count_visited = 0
        right = True
        down = False
        left = False
        up = False
        i,j = rStart,cStart
        wall = {"r" : j + 2,"d" : i + 2,"l" :j - 2,"u" : i - 2}
        res = []

        while count_visited != rows * cols:
            if right:
                while j < wall["r"]:
                    if -1 < i < rows and -1 < j < cols:
                        res.append([i,j])
                        count_visited += 1
                    j += 1
                wall["r"] += 1
                j -= 1 #fix loop 
                i += 1 #go to next
                right = not(right)
                down = not(down)
            if down:
                while i < wall["d"]:
                    if -1 < i < rows and -1 < j < cols:
                        res.append([i,j])
                        count_visited += 1 
                    i += 1
                wall["d"] += 1
                i -= 1 #fix loop 
                j -= 1 #go to next
                down = not(down)
                left = not(left)
            if left:
                while j > wall["l"]:
                    if -1 < i < rows and -1 < j < cols:
                        res.append([i,j])
                        count_visited += 1 
                    j -= 1
                wall["l"] -= 1
                j += 1 #fix loop 
                i -= 1 #go to next
                left = not(left)
                up = not(up)
            if up:
                while i > wall["u"]:
                    if -1 < i < rows and -1 < j < cols:
                        res.append([i,j])
                        count_visited += 1 
                    i -= 1
                wall["u"] -= 1
                i += 1 #fix loop 
                j += 1 #go to next
                up = not(up)
                right = not(right)
        return res
