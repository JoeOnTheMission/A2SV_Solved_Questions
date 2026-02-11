class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_version = set(nums)
        if len(set_version) ==  len(nums):
            return False
        else:
            return True
        