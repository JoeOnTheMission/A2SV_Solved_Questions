from collections import defaultdict
s = input()
stack = [] #[length]


temp = 0

for chr in s:

    if chr == "(":
        stack.append("(")

    else:#closeing
        temp = 0 #[length]

        while stack and stack[-1] != "(" and stack[-1] != ")":#its a num 
            length = stack.pop()
            temp += length 

        if stack and stack[-1] == "(":
            temp += 1
            stack.pop()
            stack.append(temp)
        else:
            stack.append(temp)
            stack.append(")")
            temp = 0
ans = []
#compres
temp = 0
res = [0,1] #[max lenght,count]
for num in stack:
    if num in ["(",")"]:
        ans.append(temp)
        
        if res[0] < temp:
            res = [temp,1]
        elif res[0] == temp:
            res[1] += 1
        temp = 0
    else:
        temp += num
    #print(ans,res)
    
if num not in ["(",")"]:
    ans.append(temp)
    if res[0] < temp:
        res = [temp,1]
    elif res[0] == temp:
        res[1] += 1

#print(ans)
if res[0] == 0:
    print(0,1)
else:
    print(res[0]*2,res[1])