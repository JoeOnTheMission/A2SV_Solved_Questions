import heapq
n = int(input())
h = [ ]
res = []
for _ in range(n):
    entry = input().split()
    if len(entry) == 1:
        op = "removeMin"
    
    else:
        op,num = entry
        num = int(num)
    
    if op == "insert":
        heapq.heappush(h,num)
       
        res.append(["insert",str(num)])
    elif op == "removeMin":
        if h:
            heapq.heappop(h)
            res.append(["removeMin"])
        else:
            res.append(["insert","0"])
            res.append(["removeMin"])

    elif op == "getMin":
        while h and h[0] < num:
                removed = heapq.heappop(h)
                res.append(["removeMin"])

        if h:
            if h[0] == num:
                res.append(["getMin",str(num)])
            if h[0] > num:
                heapq.heappush(h,num)
            
                res.append(["insert",str(num)])
                res.append(["getMin",str(num)])
        else:
            heapq.heappush(h,num)
        
            res.append(["insert",str(num)])
            res.append(["getMin",str(num)])
        
print(len(res))

for pair in res:
    
    if len(pair) == 1:
        print(pair[0])
    else:
        print(" ".join(pair))