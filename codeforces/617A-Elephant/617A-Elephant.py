dist = int(input())
res = 0 
for i in range(5,0,-1):
    
    x =  dist // i 
    dist -= (x*i)
    res += x
print(res)