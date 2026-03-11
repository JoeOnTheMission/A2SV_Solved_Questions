class RecentCounter:

    def __init__(self):
        self.requests = deque()
        
        

    def ping(self, t: int) -> int:
        self.requests.append(t)
        #print(self.requests,len(self.requests))
        #fix queue
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()
        
        return len(self.requests)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)