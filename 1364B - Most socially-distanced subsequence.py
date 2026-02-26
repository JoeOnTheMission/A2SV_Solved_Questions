t = int(input())
for _ in range(t):
    n = int(input())# this took 53 min 36 sec
    p = list(map(int,input().split()))
    res = [p[0]]
    i = 0
    if p[0] < p[1]:
        last = 1
    else:
        last = -1
    
    while i < n-1:
        if p[i] < p[i+1]:
            now = 1
        else:
            now = -1
        if last != now:
            res.append(p[i])
            last = now
        i += 1 
    res.append(p[-1]) 
    print(len(res))
    print(*res)

