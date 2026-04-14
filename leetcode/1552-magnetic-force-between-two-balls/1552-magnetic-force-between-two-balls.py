class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        #the furthest you can make and 2 consecutive balls
        position.sort()
        def helper(distance):
            #print(distance)
            nxt = position[0]
            balls = 0
            for num in position:
                if num >= nxt:
                    nxt = num + distance
                    balls += 1
                #print(num,nxt,balls)
                if balls >= m:
                    #print(True)
                    return True
                    
            #print(False)
            return False 
            

        #print(helper(4))
        left = 1
        right = position[-1] - position[0]
        while left <= right:
            mid = left + (right - left) // 2
            #print(left,mid,right)
            if helper(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right