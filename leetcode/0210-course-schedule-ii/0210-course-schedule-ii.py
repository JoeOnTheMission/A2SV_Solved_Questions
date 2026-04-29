class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0 for i in range(numCourses)]
        for v,u in prerequisites:
            graph[u].append(v)
            indegree[v]+=1
        # print(graph)
        # print(indegree)
        q = deque()
        for node,indegree_count in enumerate(indegree):
            if indegree_count == 0:
                q.append(node)
        res = []
        while q:
            cur_node = q.pop()
            res.append(cur_node)
            for child in graph[cur_node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)
        return res if len(res) == numCourses else [] 
            
