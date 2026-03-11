class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        i = 0

        while i < len(s):
            #print(s[i],stack)
            if s[i] == "(":
                stack.append(0)
                i += 1
            else:
                now = stack.pop()
                if now == 0:
                    stack[-1]+=1
                else:
                    stack[-1]+=2*now
                i += 1
            #print("after",stack)
        return stack[0]
            

            