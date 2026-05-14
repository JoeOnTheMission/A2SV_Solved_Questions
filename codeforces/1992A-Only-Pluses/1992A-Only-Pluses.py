t = int(input())
for _ in range(t):
    all_input = list(map(int,input().split()))
    all_input.sort()
    for i in range(5):
        all_input[0] += 1
        all_input.sort()
    print(all_input[0]*all_input[1]*all_input[2])