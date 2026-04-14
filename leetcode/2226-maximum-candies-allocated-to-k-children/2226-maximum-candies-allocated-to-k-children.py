class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def helper(piles):
            have = 0
            for num in candies:
                have += num//piles
            return True if have >= k else False
        left = 1
        right = max(candies)
        all_values = sum(candies)
        if all_values < k:
            return 0
        while left <= right:
            mid = left + (right-left)//2

            #print(left,mid,right,helper(mid))
            if helper(mid):
                left = mid  + 1
            else:
                right = mid - 1
        return right