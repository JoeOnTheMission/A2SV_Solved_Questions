t = int(input())
for _ in range(t):
    s = input()# 22min and 40 sec 
    i = 0
    res = set()
    doubles = set()
    if len(s) > 1:
        while i + 1 < len(s):
            if s[i] != s[i+1]:
                if s[i] not in res:
                    res.add(s[i])
                i += 1
            else:
                i += 2
        if s[-2] != s [-1]:
            if s[-1] not in res:
                res.add(s[-1])
        else:
            if s.count(s[-1]) % 2 != 0:
                if s[-1] not in res:
                    res.add(s[-1])

        print("".join(sorted(res)))
    else:
        print(s[0])
