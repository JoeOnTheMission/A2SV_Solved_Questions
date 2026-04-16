class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        res = set()
        for num in nums:
            if num in seen:
                res.add(num)
            else:
                seen.add(num)
        return list(res)