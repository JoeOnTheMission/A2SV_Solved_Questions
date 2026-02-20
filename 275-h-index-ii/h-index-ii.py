class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        for i,val in enumerate(citations):
            if n - i <= val:
                return n-i
        return 0