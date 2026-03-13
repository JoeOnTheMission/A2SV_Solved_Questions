def magic(arr):
    ans = []
    running = 0
    stack = [] #[value,count]
    for num in arr:
        count = 1
        while stack and stack[-1][0] > num:
            removed = stack.pop()
            running -= removed[0]*removed[1]
            count += removed[1]
        running += num*count
        if stack and stack[-1][0] == num:
            stack[-1][1] += count
            
        else:
            stack.append([num,count])
        ans.append(running)
    return ans
prefix = magic(m)
sufix = magic(reversed(m))[::-1]

#find best start 
best_start = [-1,-1]#[floors,index]
for i in range(n):
    floor_count = prefix[i] + sufix[i] - m[i]
    if best_start[0] < floor_count:
        best_start = [floor_count,i]
#build answer
final = [0]*n
minimum = float("inf")
for i in range(best_start[1],n):#forward
    minimum = min(minimum,m[i])
    final[i] = minimum
minimum = float("inf")
for i in range(best_start[1],-1,-1):#backward
    minimum = min(minimum,m[i])
    final[i] = minimum
print(*final)