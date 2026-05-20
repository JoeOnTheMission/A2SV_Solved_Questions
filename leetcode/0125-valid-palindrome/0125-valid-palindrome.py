class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        a = [char for char in s if char.isalnum()]
        l = 0
        r = len(a) - 1
        while l < r:
            if a[l] != a[r]:
                return False
            l += 1
            r -= 1
        return True 