from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()


    res = n + 1
    
    for i in range(n):
        for length in range(2,8):
            a_count = 0
            b_count = 0
            c_count = 0
            if i + length > n:
                break
            sub = s[i : i + length]
            for letter in sub:
                if letter == "a":
                    a_count += 1
                elif letter == "b":
                    b_count += 1
                else:
                    c_count += 1
            if a_count > max(b_count,c_count): 
                res = min(res,length)
    
    print(res if res != len(s)+1 else -1)
