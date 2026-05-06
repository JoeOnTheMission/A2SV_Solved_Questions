class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) >= 2:
            y = heapq.heappop_max(stones)
            x = heapq.heappop_max(stones)
            if x != y:
                new = y-x
                heapq.heappush_max(stones,new)
            # print(y,x)
            # print(stones)
        if len(stones) == 0:
            return 0
        return stones[0]