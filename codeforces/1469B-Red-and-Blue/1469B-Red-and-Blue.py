t = int(input())
for _ in range(t):
    n = int(input())
    red = list(map(int,input().split()))
    m = int(input())
    blue = list(map(int,input().split()))

    pre_red_max = 0
    running_red = 0
    for i in range(n):
        running_red += red[i]
        pre_red_max = max(pre_red_max,running_red)
        
    

    pre_blue_max = 0
    running_blue = 0
    for i in range(m):
        running_blue += blue[i]
        pre_blue_max = max(pre_blue_max,running_blue)
    
    print(max(0,pre_red_max+pre_blue_max))