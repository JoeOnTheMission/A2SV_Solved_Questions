class Solution:
    def hIndex(self, citations: List[int]) -> int:
        counts = [0]*len(citations)
        for num in citations:
            index = 0 
            while index < len(counts) and  index < num:
                counts[index] += 1
                index += 1
        res = [0]
        for i,count in enumerate(counts):
            if i + 1 <= count :
                res.append(i+1)
        return max(res)
                