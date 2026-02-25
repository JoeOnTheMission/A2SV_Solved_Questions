t = int(input())
for _ in range(t):
    s = input()
    t = input()
    s_sorted = sorted(s)
    t_sorted = sorted(t)
    temp = []
    i = 0# for t_sorted
    j = 0
    #print(s_sorted)
    #print(t_sorted)
    while j < len(s_sorted) and i < len(t_sorted):
        if t_sorted[i] == s_sorted[j]:
            j += 1
        else:
            temp.append(t_sorted[i])
        i += 1
    temp.extend(s_sorted[j:])
    temp.extend(t_sorted[i:])
    #print(len(s_sorted),j)
    if len(s_sorted) != j:
        print("Impossible")
    else:
            
        i = 0#this is for s
        j = 0# this is for temp
        res = []
        while i < len(s) and j < len(temp):
            if s[i] <= temp[j]:
                res.append(s[i])
                i += 1
            else:
                res.append(temp[j])
                j += 1
       
        res.extend(s[i:])
        res.extend(temp[j:])
        print("".join(res))
