class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if (num-3) % 3 == 0:#possible
            x = (num-3)//3
            res = [x+n for n in range(3)]
            return res
        else:
            return []
            
        