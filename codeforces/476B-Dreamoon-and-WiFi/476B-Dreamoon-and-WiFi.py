#print(end)

def recursive(index,now):
    if index == n:
        #reached bottom
        #print(now)
        if now == end:
            final[0] += 1
        else:
            final[1] += 1
        return
    if recived[index] == "+":
        now += 1
        recursive(index + 1,now)
    elif recived[index] == "-":
        now -= 1
        recursive(index + 1,now)
    else:# ?
        for i in [-1,1]:
            now += i
            recursive(index+1,now)
            now -= i
recursive(0,0)
all = final[0] + final[1]
print(final[0]/all)