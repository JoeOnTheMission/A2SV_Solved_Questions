class Solution:
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()
        
        def can(radius):
            for house in houses:
                i = bisect_left(heaters, house)
                
                left_dist = float('inf')
                right_dist = float('inf')
                
                if i > 0:
                    left_dist = house - heaters[i - 1]
                if i < len(heaters):
                    right_dist = heaters[i] - house
                
                if min(left_dist, right_dist) > radius:
                    return False
            
            return True
        
        low, high = 0, max(max(houses),max(heaters))
        
        while low < high:
            mid = (low + high) // 2
            if can(mid):
                high = mid
            else:
                low = mid + 1
        
        return low