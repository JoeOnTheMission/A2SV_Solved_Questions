t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    line = input()

    window = [0,0] # [wight,black]
    #build window 
    for i in range(k):
        if line[i] == "W":
            window[0] += 1
        else:
            window[1] += 1
    res = window[0]
    for j in range(n-k):
        left = j
        right = j + k
        if line[left] == "W":
            window[0] -= 1
        else:
            window[1] -= 1

        if line[right] == "W":
            window[0] += 1
        else:
            window[1] += 1
        
        res = min(res,window[0])
    print(res)  
