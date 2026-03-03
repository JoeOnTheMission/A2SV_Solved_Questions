# build pre
for i in range(1,len(pre)):
    pre[i] += pre[i-1]
# make valid ones 1 and other 0
for i in range(len(pre)):
    if pre[i] >= k:
        pre[i] = 1 
    else:
        pre[i] = 0
# build new pre
for i in range(1,len(pre)):
    pre[i] += pre[i-1]
for question in range(q):
    l,r = map(int,input().split())
    print(pre[r]- pre[l-1])