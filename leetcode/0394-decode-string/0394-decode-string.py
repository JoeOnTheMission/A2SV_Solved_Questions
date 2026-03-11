class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []#[num,start]

        i = 0
        while i < len(s):
            if s[i].isdigit():#see a number 
                digit = []
                while s[i] != "[":
                    digit.append(s[i])
                    i += 1
                stack.append("".join(digit))
                i += 1 #skip "["

            elif s[i] != "]":
                stack.append(s[i])
                i += 1
            else:#found "]"
                
                now = []
                while stack and not(stack[-1].isdigit()) :#until i see a num pop from stack
                    now.append(stack.pop())
                now.reverse()
                
                final =int(stack[-1])*"".join(now)
                stack.pop()
                stack.append(final)
                i += 1
        return "".join(stack)
                    