class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for i in range(len(names)):
            m = i
            for j in range(i ,len(names)):
                if heights[m] < heights[j]:
                    m = j
            heights[m],heights[i] = heights[i],heights[m]
            names[m],names[i] = names[i],names[m]
        return names