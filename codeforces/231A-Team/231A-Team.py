n = int(input())
res = 0
for _ in range(n):
    x,y,z = map(int,input().split())
    
    if x+y+z > 1:
        res += 1
    
print(res)