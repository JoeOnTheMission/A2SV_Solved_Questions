from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    graph = list(map(int,input().split()))
    indegree = [0 for _ in range(n)]
    for u,v in enumerate(graph):
        indegree[v-1] += 1
        graph[u] = v-1

    q = deque()

    for index,indegree_count in enumerate(indegree):
        if indegree_count == 0:
            q.append(index)
    year = 2
    while q:
        year += 1
        for i in range(len(q)):
            cur = q.popleft()
            indegree[graph[cur]] -= 1
            if indegree[graph[cur]] == 0:
                q.append(graph[cur])
            # print(cur)
            # print(indegree,year)
    print(year)