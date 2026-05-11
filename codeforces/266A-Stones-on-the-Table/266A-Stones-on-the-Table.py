# print(i,j,res)
    if rocks[i] == rocks[j]:
        j += 1
        res += 1
    else:
        i = j
        j += 1
print(res)