from collections import Counter
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_counts = Counter(a)
b_counts = Counter(b)
base = a_counts if len(a_counts) <= len(b_counts) else b_counts
other = b_counts if len(a_counts) <= len(b_counts) else a_counts
res = 0
for num in base:
    if num in other:
        res += (a_counts[num] * b_counts[num])
print(res)
