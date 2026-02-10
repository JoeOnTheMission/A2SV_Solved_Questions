class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        neededs =[]
        for num in nums:
            needed = target - num
            neededs.append(needed)

        for x in range(len(nums)):
            for y in range(len(neededs)):
                if x == y:
                    continue
                elif nums[x] == neededs[y]:
                    return [x,y]
                    