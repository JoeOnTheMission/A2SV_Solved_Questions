class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #this took 7 min
        n = len(citations)
        for i,val in enumerate(citations):
            if n - i <= val:
                return n-i
        return 0
