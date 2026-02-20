t = int(input())
for _ in range(t):
    n,k = list(map(int,input().split()))
    casinos = []
    for _ in range(n):
        casino = list(map(int,input().split()))
        casinos.append(casino)
    #casinos.sort(key=lambda cas: (cas[0],cas[1],-cas[2]))
    casinos.sort()
    max_real = 0
    for cas in casinos:
        if cas[0] > k or k > cas[1]:#out of bound
            k = max(k,max_real)
        if cas[0] <= k <= cas[1]:
            max_real = max(max_real,cas[2])
    print(max(k,max_real))
