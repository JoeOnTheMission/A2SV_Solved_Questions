class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        initial = x
        final = 0
        while x:
            y = x%10
            final = (final * 10) + y
            x //= 10
        if final == initial:
            return True
        else:
            return False
            
        
            