class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = [[0]*len(heights[0]) for _ in range(len(heights))]

        def flow(i,j,pacific,atlantic):
    
            #print(i,j,pacific,atlantic)
            if pacific and atlantic:
                return [pacific,atlantic]
            
            visited[i][j] = 1

            now = heights[i][j]
            #print("now",now)
            
            for i_change,j_change in directions:
                new_i = i+i_change
                new_j = j+j_change

                #print(new_i,new_j)

                if new_i < 0 or new_j < 0:#touches pacific
                    pacific = pacific or True

                    #print("pacific")

                elif new_i >= len(heights) or new_j >= len(heights[0]):#touches atlantic
                    atlantic = atlantic or True

                    #print("atlantic")

                elif heights[new_i][new_j] <= now:#we can go in this direction
                    if visited[new_i][new_j] == 0:#not visited
                        #print("next",heights[new_i][new_j])

                        a1,a2 = flow(new_i,new_j,pacific,atlantic)
                        pacific = pacific or a1
                        atlantic = atlantic or a2
           
            visited[i][j] = 0

            return [pacific,atlantic]
        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                #print("input",i,j)
                pacific,atlantic = flow(i,j,False,False)
                #print("output",pacific,atlantic)
                if pacific and atlantic:
                    res.append([i,j])
        return res