class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = defaultdict(int)
        res = set()
        for num in nums:
            counter[num] += 1
            if num not in res and counter[num] > len(nums)//3:
                res.add(num)
        return list(res)