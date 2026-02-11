class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        sum = 0
        for num in nums:# build initial even nums sum
            if num % 2 == 0:
                sum += num

        for val,i in queries:# goes through the queries 
            old = nums[i]
            nums[i] = nums[i] + val
            new = nums[i]

            if old % 2 == 0:# old is even
                sum -= old
                if new % 2 == 0:# new is even 
                    sum += new
            else:# old is odd
                if new % 2 == 0:# new is even
                    sum += new
            res.append(sum)
        return res