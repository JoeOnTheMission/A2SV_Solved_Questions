class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        i = 0
        j = -1
        done = False
        
        while not done:
            op = 0
            for i in range(len(names)+j):
                if heights[i] < heights[i+1]:
                    heights[i],heights[i+1] = heights[i+1],heights[i]
                    names[i],names[i+1] = names[i+1],names[i]
                    op += 1
            j -= 1
            if op == 0:
                done = True
        return names
