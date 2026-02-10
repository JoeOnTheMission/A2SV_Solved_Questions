t = int(input())
for _ in range(t):
    n,x,k = map(int,input().split())
    s = input()
    now = x
    steps_to_zero = 0
    res = 0
    for op in s:
        if op == "L":
            now -= 1
        else:#right 
            now += 1
        steps_to_zero += 1

        if now == 0:# reached zero
            res += 1
            break

    if steps_to_zero > k or res == 0:# not valid or finished with out reaching zero
        print(0)
    else:
        # find loop length 
        now = 0
        steps_to_loop = 0
        for op in s:
            if op == "L":
                now -= 1
            else:#right 
                now += 1
            steps_to_loop += 1

            if now == 0:# reached zero
                res += 1
                break
        
        if steps_to_loop > k - steps_to_zero or res == 1:# not valid or finished with out reaching zero
            print(1)
        else:# answer different form zero and one
            res = (k - steps_to_zero)//steps_to_loop
            res += 1 # for the fist found zero before loop 
            print(res)
