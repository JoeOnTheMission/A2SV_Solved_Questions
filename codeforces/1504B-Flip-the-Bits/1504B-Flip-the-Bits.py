#build the prefix sum of a 
    prefix=[int(a[0])]
    for i in range(1, n):
        prefix.append(prefix[i-1]+int(a[i]))

    flip=0
    flag=1

    for i in range(n-1, -1, -1):
        if (not flip and a[i]==b[i]) or (flip and a[i]!=b[i]):# we are fine 
            continue
        
        if not flip and a[i]!=b[i] and prefix[i]==i+1-prefix[i]:# mis match but we can flip
            # print(prefix[i], n)
            flip=int(not flip)
        elif flip and a[i]==b[i] and prefix[i]==i+1-prefix[i]:# mis match but we can flip
            flip=int(not flip) 
        else:# mis match and we can not flip 
            flag=0
            break
    

    if flag:
        print("YES")
    else:
        print('NO')