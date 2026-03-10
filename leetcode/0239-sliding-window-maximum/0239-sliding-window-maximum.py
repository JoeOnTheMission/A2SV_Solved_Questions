class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #build window:
        queue = deque()
        res = []
        for i in range(k):
            while queue and nums[i] > queue[-1]:
                queue.pop()
            queue.append(nums[i])
        res.append(queue[0])
        
        #slide the window 
        for i in range(len(nums)-k):
            #remove nums[i] from stack
            if queue and nums[i] == queue[0]:
                queue.popleft()

            

            #add nums[i+1] to the stack
            while queue and nums[i+k] > queue[-1]:#find its place
                queue.pop()
            queue.append(nums[i+k])
            res.append(queue[0])
            
            
        return res
