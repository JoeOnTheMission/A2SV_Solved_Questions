found = False
for r in range(5):
    
    row = list(map(int,input().split()))
    for c in range(5):
        if row[c] == 1: 
            found = True
            break
    if found:
        break

print(abs(r-2)+abs(c-2))

    
