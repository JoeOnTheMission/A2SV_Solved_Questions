n = int(input())
res = 0 
for _ in range(n):
    li = list(input())
    i = 0
    while i < len(li):
        if li[i] == "-":
            i += 2
            res -= 1
        elif li[i] =="+":
            i += 2
            res += 1
        else:
            i += 1
print(res)