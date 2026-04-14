class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def helper(capacity):
            running = 0
            count = 1
            #all = []
            for num in weights:
                running += num
                #print(num,running,count)
                
                if running > capacity:
                    #all.append(running - num)
                    count += 1
                    running = num
                    #print(all)
                if count > days:
                    return False
            return True
        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = (low + high)//2

            if helper(mid):

                high = mid - 1 
            else:
                low = mid + 1

        return low
        