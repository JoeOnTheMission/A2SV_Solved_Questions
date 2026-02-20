n,k = map(int,input().split())
a = list(map(int,input().split()))

op = n - k - 2
values = []
for i in range(n-1):
    x = a[i]
    y = a[i + 1]
    values.append(y-x)
values.sort()
res = sum(values)
print(sum(values[:n-k]))
