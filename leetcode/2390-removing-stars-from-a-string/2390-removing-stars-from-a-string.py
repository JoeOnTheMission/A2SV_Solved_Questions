class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for chr in s:
            if chr == "*":
                if stack:
                    stack.pop()
            else:
                stack.append(chr)
        return "".join(stack)