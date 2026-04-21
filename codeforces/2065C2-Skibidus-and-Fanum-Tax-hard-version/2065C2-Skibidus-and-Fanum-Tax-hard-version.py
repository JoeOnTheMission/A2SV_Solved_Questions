from bisect import bisect_left
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    #b.append(0)
    b.sort()

    prev = float("-inf")
    can =  True
    for i in range(n):
        cur = a[i]
        target = prev + cur
        it_idx = bisect_left(b, target)

        option_a = cur if cur >= prev else float("inf")
        option_b = (b[it_idx] - cur) if it_idx < m else float("inf")

        best = min(option_a,option_b)

        if best == float("inf"):
                can = False
                break
        prev = best
    if can:
        print("YES")
    else:
        print("NO")