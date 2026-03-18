class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = defaultdict(int)
        full = []
        for r in answers:
            if count[r] >= r+1:#full
                count[r] = 1
                full.append(r)
            else:
                count[r] += 1
            #print(r)
            #print(full,count)
        res = 0
        #print(full,count)
        for num in full:
            #print(num+1)
            res += (num + 1)
        for num in count.keys():
            #print(num+1)
            res += (num +1)
        return res



