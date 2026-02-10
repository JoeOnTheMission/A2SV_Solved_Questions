class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            digits = []
            while num >= 10:
                digit = num % 10 
                num = num // 10 
                digits.append(digit)
            digits.append(num)
            digits.reverse()
            res.extend(digits)
        return res