from collections import defaultdict
n,k = map(int,input().split())
a = list(map(int,input().split()))

left = 0
window = defaultdict(int)
count_valid = 0

for right in range(n):
    window[a[right]] += 1
    while len(window) > k:#in valid 
        window[a[left]] -= 1
        if window[a[left]] == 0:
            window.pop(a[left])
        left += 1
       
    count_valid += right - left + 1
print(count_valid) 
