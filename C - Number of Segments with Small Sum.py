n,s = map(int,input().split())
a = list(map(int,input().split()))

left = 0
window = 0
count_of_valid = 0

for right in range(len(a)):
    
    window += a[right]
    while window > s:# invalid
        window -= a[left]
        left += 1
    n = right - left + 1
    count_of_valid += n

print(count_of_valid)
