class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        #tasks.sort()
        # i = 0 #next task not in waiting
        all_tasks = []#heap (en_time,cost,index)
        waiting = []#heap (cost,index)
        time = 1
        res = []
        for i , val in enumerate(tasks):
            en_time,cost = val
            heapq.heappush(all_tasks,(en_time, cost, i))
        #print(all_tasks[0][0])
        while all_tasks:
            while all_tasks and all_tasks[0][0] <= time:
                en_time, cost, index = heapq.heappop(all_tasks)
                heapq.heappush(waiting,(cost,index))
                
            if waiting:
                cost, index = heapq.heappop(waiting)
                time += cost
                res.append(index)
           
            else:#idel and no waiting but still their are tasks
                time = all_tasks[0][0]
        
        while waiting:#catch whatever is left
            cost, index = heapq.heappop(waiting)
            # time += cost
            res.append(index)

        return res
                               