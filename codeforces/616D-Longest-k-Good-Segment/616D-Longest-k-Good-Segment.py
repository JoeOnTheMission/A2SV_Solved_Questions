from collections import defaultdict
n,k = map(int,input().split())
a = input().split()
unique =  defaultdict(int)

left = 0
res = []
max_length = 0
for right in range(n):
    unique[a[right]] += 1
    while len(unique) > k:#shrink 
        unique[a[left]] -= 1
        if unique[a[left]] == 0:
            unique.pop(a[left])
        left += 1
    # valid 
    if max_length < right - left  + 1:#update
        max_length = right - left + 1
        res = [left+1,right+1]
print(*res)