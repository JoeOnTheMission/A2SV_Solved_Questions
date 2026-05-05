from collections import deque
n = int(input())
names = []
s = input()
names.append(s)

graph = [[] for _ in range(26)]
indegree = [0] * 26

def converter(value,to_number):
    offset =  ord('a')
    if to_number:#change in to number
        return ord(value) - offset
    else:
        return chr(value + offset)

for _ in range(n-1):
    t = names[-1]
    s = input()
    names.append(s)
    j = 0

    while j < len(t) and j < len(s) and s[j] == t[j]:#find the first different
        j += 1

    if j < len(s) and j < len(t):
        graph[converter(t[j],True)].append(converter(s[j],True))
        indegree[converter(s[j],True)] += 1
    elif j < len(s):
        #we can't extract any thing from this
        continue
    else:
        print("Impossible")
        exit()
    # print(graph)
    # print(indegree)
if len(names) <= 1:
    print("bcdefghijklmnopqrsatuvwxyz")
else:
    q = deque()
    for index,indegree_count in enumerate(indegree):
        if indegree_count == 0:
            q.append(index)
    res = []
    while q:
        cur = q.popleft()
        res.append(converter(cur,False))

        for child in graph[cur]:
            indegree[child] -= 1
            if indegree[child] == 0:
                q.append(child)
    if len(res) == 26:
        print("".join(res))
    else:
        print("Impossible")