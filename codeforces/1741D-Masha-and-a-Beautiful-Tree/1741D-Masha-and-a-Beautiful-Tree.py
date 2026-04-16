def mergesort(arr):
        #print(arr)
        if not can[0]:
            return [- 1]
        if len(arr) <= 1:
            return arr
        
        split = len(arr)//2
        left = mergesort(arr[:split])
        right = mergesort(arr[split:])
        
        if left[-1] + 1 == right[0]:#yes
            return left + right
        elif right[-1] + 1 == left[0]:
            opp[0] += 1 
            return right + left      
        else:
            can[0] = False
            return [-1]
        

    mergesort(p)
    if can[0]:
        print(opp[0])
    else:
        print(-1)