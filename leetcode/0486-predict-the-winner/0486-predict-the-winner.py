class Solution:
    def choice(self,i,j):
        if i == j:
            return self.arr[i]
        option1 = self.arr[i] - self.choice(i+1,j)#choose i
        option2 = self.arr[j] - self.choice(i,j-1)#choose j
        return  max(option1,option2)
    def predictTheWinner(self, nums: List[int]) -> bool:
        self.arr = nums
        return self.choice(0,len(nums)-1) >= 0
        
        