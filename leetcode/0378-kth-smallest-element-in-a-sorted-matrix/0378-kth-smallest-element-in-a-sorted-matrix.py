class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        h = [num for row in matrix for num in row]
        heapq.heapify(h)
        res = heapq.nsmallest(k,h)
        return res[-1]