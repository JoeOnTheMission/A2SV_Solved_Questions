class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        res = 0
        i = 1
        count = 0
        while  count < len(piles)//3:
            res += piles[i]
            i+=2
            count += 1
        return res