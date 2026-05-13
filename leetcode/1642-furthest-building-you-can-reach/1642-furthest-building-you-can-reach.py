class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        h = []
        last = heights[0]
        total = 0
        step = 0
        ladder_ones = 0
        for i in range(1,len(heights)):
            num = heights[i] 
            last = heights[i-1]
            # print(num,last)
            if last >= num:
                # print(0)
                continue
            else:
                step = num-last
            # print(step)

            heapq.heappush(h,step)
            ladder_ones += step
            if len(h) > ladders:
                x = heapq.heappop(h)
                ladder_ones -= x

            total += step
         
            # print(ladder_ones,step)
            # print("index",i,"ladder",ladder_ones,"total",total,"brick",total-ladder_ones)
            if total - ladder_ones > bricks:
                # print("no")
                return i-1
        return len(heights)-1