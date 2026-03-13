class Solution:
    def minOperations(self, nums: List[int]) -> int:
        pre = [x for x in nums]
        res = 0
        can = True
        for i in range(len(nums)-2):
            if pre[i]%2 == 0:
                pre[i] += 1
                pre[i+1] += 1
                pre[i+2] += 1
                res += 1
        else:
            for i in range(-1,-4,-1):
                if pre[i] % 2 == 0:
                    can = False
              
        if can:
            return res
        return -1


