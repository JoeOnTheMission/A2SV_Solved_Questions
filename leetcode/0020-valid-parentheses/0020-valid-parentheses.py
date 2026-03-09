class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = {'(','{','['}
        pair = { ')':"(" ,  '}':'{'  , ']':'[' }
        for sign in s:
            if sign in opening:
                stack.append(sign)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] != pair[sign]:
                    return False
                else:
                    stack.pop()
        else:
            if len(stack) == 0:
                return True 
            else:
                return False
