class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        valid2 = [0]*len(heights)
        stack = []
        for i in range(len(heights)-1,-1,-1):
            #print(heights[i],stack)
        
            while stack and heights[stack[-1]-1] >= heights[i]:
                stack.pop()
            
            if stack: 
                valid2[i] = stack[-1]
            else:
                valid2[i] = len(heights)+1
            stack.append(i+1)
        #print("valid",valid2)

        valid = [0]*len(heights)
        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]-1] >= heights[i]:
                stack.pop()
            #print(stack)
            if stack: 
                valid2[i] -= stack[-1]
          
            valid2[i] -= 1
            stack.append(i+1)
        #print("valid",valid2)
        res = 0
        for i in range(len(heights)):
            res = max(res,valid2[i]*heights[i])
        return res