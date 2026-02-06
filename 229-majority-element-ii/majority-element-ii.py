class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
    
        d = Counter(nums)
        n = len(nums)
        res =[]
        for num in d:
            if d[num] > n//3:
                res.append(num)
        return res