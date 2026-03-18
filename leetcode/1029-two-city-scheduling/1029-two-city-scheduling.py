class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key= lambda x:[(x[0]-x[1]),x[0]])
        res = 0
        for i,pair in enumerate(costs):
            
            if i < len(costs)//2:
                res += pair[0]
            else:
                res += pair[1]
        return res
