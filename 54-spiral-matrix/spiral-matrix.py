class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        right = True
        down = False
        left = False
        up = False
        i = 0 
        j = 0
        wall = {"r" : len(matrix[0]),"d" : len(matrix),"l" : -1,"u" : -1}
        done = False

        while not done:

            if right:
                while j < wall["r"]:
                    res.append(matrix[i][j])
                    j += 1
                wall["u"] = i
                j -= 1 #fix the while loop
                i += 1 #already added to res so skip it
                right = False
                down = True
        
                
                
                
            elif down: 
                while i  < wall["d"]:
                    res.append(matrix[i][j])
                    i += 1
                wall["r"] = j
                j -= 1 #fix the while loop
                i -= 1 #already added to res so skip it
                down = False
                left = True
                
                
            elif left: 
                while j  > wall["l"]:
                    res.append(matrix[i][j])
                    j -= 1
                wall["d"] = i
                j += 1 #fix the while loop
                i -= 1 #already added to res so skip it
                left = False
                up = True

                
            elif up: 
                while i  > wall["u"]:
                    res.append(matrix[i][j])
                    i -= 1
                wall["l"] = j
                i += 1 #fix the while loop
                j += 1 #already added to res so skip it
                up = False
                right = True
            
            if not (wall["u"] < i < wall["d"]) or not (wall["l"] < j < wall["r"]):
                done = True
        return res
