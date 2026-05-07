class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n+1)]
        indegree  = [0]*(n+1)
        m_time = [0]*(n+1)
        for u,v in relations:
            graph[u].append(v)
            indegree[v] += 1
    
        q = deque()

        for i in range(1,n+1):
            if indegree[i] == 0:
                q.append(i)
                m_time[i] = time[i-1]
        while q:
            cur = q.popleft()

            for adj in graph[cur]:
                m_time[adj] = max(m_time[adj],m_time[cur] + time[adj-1])
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    q.append(adj)


        return max(m_time)