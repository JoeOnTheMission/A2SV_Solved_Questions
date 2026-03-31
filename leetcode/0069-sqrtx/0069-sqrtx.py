class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        res = 0
        if x == 1:
            return 1
        while left <= right:
            
            mid = (left + right)//2
            now = mid**2
            #print(left,right,mid)
            #print(abs(res**2-x),abs(now-x))
            if abs(res**2-x) >= abs(now-x) and now <= x:
                res = mid
            if now > x:
                right = mid - 1
            elif now < x:
                left = mid + 1
            else:
                
                break
        return res