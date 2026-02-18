class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s = [str(num) for num in nums] 
        for i in range(len(s)):
            for j in range(len(s)-1):
                if s[j+1]+s[j] > s[j]+s[j+1]:
                    s[j],s[j+1] = s[j+1],s[j]
        res = "".join(s)
        return str(int(res))