n,s = map(int,input().split())
a = list(map(int,input().split()))

left = 0 
window = 0
count_of_Valid = 0

for right in range(n):
    window += a[right]
    while window >= s:#valid
        window -= a[left]
        count_of_Valid += n - right
        left += 1
print(count_of_Valid)
