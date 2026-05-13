s = input()
count = [0,0]#[upper,lower]
for letter in s:
    if letter.isupper():
        count[0] += 1
    else:
        count[1] += 1
if count[0] > count[1]:
    print(s.upper())
else:
    print(s.lower())