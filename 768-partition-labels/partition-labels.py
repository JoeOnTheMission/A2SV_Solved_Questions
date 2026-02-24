class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i,letter in enumerate(s):
            d[letter] = i
        #print(d)
        i = 0
        res = []
        max_sub = d[s[0]]
        last = 0
        for i,letter in enumerate(s):
            max_sub = max(max_sub,d[letter])
            if i == max_sub:
                if len(res) == 0:# the first one
                    res.append(i + 1)
                else:
                    res.append(i-last)
                last = i
           
        if i == max_sub and last != i:
                if len(res) == 0:# the first one
                    res.append(i + 1)
                else:
                    res.append(i-last)
        return res 