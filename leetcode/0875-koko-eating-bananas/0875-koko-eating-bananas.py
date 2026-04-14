class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(k):
            runnig = 0
            hours = 0
            
            for num in piles:
                
                if num % k == 0:
                    x = 0
                else:
                    x = 1
                hours += num // k + x

                #print(num,num // k + x)
                if hours > h:
                    return False
            return True
        #print(helper(4))
        low = 1
        high = max(piles)
        while low <= high:
            mid = (low + high)//2

            if helper(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low