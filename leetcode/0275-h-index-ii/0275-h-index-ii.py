class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        def helper(h):
            i  = bisect_left(citations,h)
            print(i)
            if n - i >= h:
                return True
            return False
        low = 0
        high = citations[-1]
        while low <= high:
            mid = low + (high - low)//2
            if helper(mid):
                low = mid + 1
            else:
                high = mid - 1
                
        return high