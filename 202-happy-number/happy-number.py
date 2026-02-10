class Solution:
    def isHappy(self, n: int) -> bool:
        loop = False
        seen = set()
        while not loop:
            sum = 0
            while n >= 10:
                digit = n % 10
                n = n // 10
                sum += digit**2
            sum += n**2
           
            if sum == 1:
                return True
            elif sum in seen:
                return False
            else: # didn't loop yet 
                seen.add(sum)
                n = sum 