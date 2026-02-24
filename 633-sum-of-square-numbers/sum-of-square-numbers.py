class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        perfects = [0,1]
        i = 2
        while perfects[-1] < c:# build all perfects i could  need 
            perfects.append(i**2)
            i += 1
        left = 0 
        right = len(perfects)-1
        while left <= right:# find target sum 
            current_sum = perfects[left] + perfects[right]
            if current_sum == c:
                return True
            elif current_sum > c:
                right -= 1
            else:
                left += 1
        return False
                    