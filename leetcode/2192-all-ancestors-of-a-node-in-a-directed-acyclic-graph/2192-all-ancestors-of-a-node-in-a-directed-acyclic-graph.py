class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = [0 for i in range(n)]
        res  = [set() for i in range(n)]
        for u,v in edges:
            graph[u].append(v)
            indegree[v] += 1
    
        q = deque()
        for i,val in enumerate(indegree):
            if val == 0:
                q.append(i)

        while q:
            #print(q)
           
            cur = q.popleft()
            ancestors = res[cur].copy()
            ancestors.add(cur)
            
            for neighbor in graph[cur]:
                #print("n",neighbor)
                res[neighbor].update(ancestors)
                
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
            #print(res)
        for i,li in enumerate(res):
            res[i] = sorted(li)
        return res
