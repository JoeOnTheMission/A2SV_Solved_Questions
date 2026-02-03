def swap_case(s):
    answer = ""
    for letter in s:
        if letter.isupper():
            answer += letter.lower()
        else:
            answer += letter.upper()
    return answer

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
