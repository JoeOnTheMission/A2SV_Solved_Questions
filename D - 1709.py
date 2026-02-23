t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    res = []
    for i in range(len(a)):
        swap = False
        for j in range(len(a)- i - 1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                swap = True
                res.append([1,j + 1])
        if not swap:
            break
        
    for i in range(len(b)):
        swap = False
        for j in range(len(a)- i - 1):
            if b[j] > b[j+1]:
                b[j],b[j+1] = b[j+1],b[j]
                swap = True
                res.append([2 ,j + 1])

        if not swap:
            break
    for i in range(len(a)):
        if a[i] > b [i]:
            a[i],b[i] = b[i],a[i]
            res.append([3,i + 1])
    print(len(res))
    for answer in res:
        print(*answer)
