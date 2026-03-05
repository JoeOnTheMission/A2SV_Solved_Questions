#print(horizontal)

#complete the horzontal prefixsum of valid starts 
for i in range(1, len(horizontal)):
    for j in range(1, len(horizontal[0])):
        horizontal[i][j] += horizontal[i - 1][j] + horizontal[i][j - 1] - horizontal[i - 1][j - 1]
#print(horizontal)

#identify valid starts for vertical 
vertical = [([0] * (c + 1)) for _ in range(r + 1)]
for i in range(r):
    for j in range(c):
        if grid[i][j] == "." and i + 1 < r and grid[i + 1][j] == ".":
            vertical[i + 1][j + 1] = 1
#print(vertical)

#complete the vertical prefixsum of valid starts 
for i in range(1, len(vertical)):
    for j in range(1, len(vertical[0])):
        vertical[i][j] += vertical[i - 1][j] + vertical[i][j - 1] - vertical[i - 1][j - 1]

q = int(input())
for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    h = (horizontal[r2][c2 - 1] - horizontal[r1 - 1][c2 - 1]- horizontal[r2][c1 - 1]+ horizontal[r1 - 1][c1 - 1])
    v = (vertical[r2 - 1][c2] - vertical[r1 - 1][c2] - vertical[r2 - 1][c1 - 1] + vertical[r1 - 1][c1 - 1])
    print(h + v)