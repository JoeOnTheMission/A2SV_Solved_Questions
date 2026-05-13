class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.n = k
        self.h = []
        for num in nums:
            heapq.heappush(self.h,num)
    
            if len(self.h) > self.n:
                heapq.heappop(self.h)

    def add(self, val: int) -> int:
        heapq.heappush(self.h,val)
        if len(self.h) > self.n:
            heapq.heappop(self.h)
        return self.h[0]
        
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)