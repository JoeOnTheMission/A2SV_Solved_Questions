class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        i = 0
        res = 0
        while i < len(points):
            left = points[i][0]
            right = points[i][1]
            i += 1
            
            while i < len(points) and  points[i][0] <= right:# intersects
                left = max(left,points[i][0])
                right = min(right,points[i][1])
                i += 1
            res += 1
        return res
