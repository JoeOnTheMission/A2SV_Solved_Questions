class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 0#max length seen
        left  = 0 
        increasing_queue = deque()
        decreasing_queue = deque()
        for right in range(len(nums)):
            #add to increasing
            while increasing_queue and nums[right] < increasing_queue[-1]:
                increasing_queue.pop()
            increasing_queue.append(nums[right])
            #print(increasing_queue)
            #add to decreasing
            while decreasing_queue and nums[right] > decreasing_queue[-1]:
                decreasing_queue.pop()
            decreasing_queue.append(nums[right])
            #print(decreasing_queue)
            absolute_dif = abs(decreasing_queue[0] -  increasing_queue[0])
            while abs(decreasing_queue[0] -  increasing_queue[0]) > limit:#shirink until valid
                #remove the left from increasing
                if increasing_queue[0] == nums[left]:
                    increasing_queue.popleft()
                #remove the left from decreasing
                if decreasing_queue[0] == nums[left]:
                    decreasing_queue.popleft()
                left += 1
            #valid ones make it here
            res = max(res,right-left+1)
        return res