class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def backtrack(index,comb):
            if len(comb) > 1:
                ans.append(comb[:])

            used = set()

            for i in range(index,n):
                if comb and nums[i] < comb[-1]:
                    continue
                if nums[i] in used:
                    continue
                used.add(nums[i])
                comb.append(nums[i])
                backtrack(i+1,comb)
                comb.pop()
        backtrack(0,[])
        return ans