class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        doubles = set()
        now = target
        while now > 1 and maxDoubles > 0:
            now = now//2
            doubles.add(now)
            maxDoubles -= 1
        doubles.add(target)
        doubles = sorted(doubles)
        res = 0
        for i in range(len(doubles)-1):
            res += doubles[i+1]-(doubles[i]*2)+1
        #print(doubles,res,doubles[0]-1)
        res += doubles[0]-1
        return res
            
        #print(doubles[i],doubles[i+1],doubles[i+1]-(doubles[i]*2)+1)

        """cur = 1
        res = 0
        print(doubles)
        while cur < target:
            if cur in doubles:
                cur = cur*2
            else:
                cur += 1
            res += 1
        return res"""