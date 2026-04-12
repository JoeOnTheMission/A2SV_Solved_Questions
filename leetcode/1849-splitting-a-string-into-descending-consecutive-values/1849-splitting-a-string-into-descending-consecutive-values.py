class Solution:
    def splitString(self, s: str) -> bool:
        
        def backtrack(index, prev):
            if index == len(s):
                return True
            
            num = 0
            for i in range(index, len(s)):
                num = num * 10 + int(s[i])
                if prev == -1:
                    if backtrack(i + 1, num):
                        return True
                else:
                    if prev - num == 1:
                        if backtrack(i + 1, num):
                            return True
                
            return False
            
        for i in range(1, len(s)):
            first = int(s[:i])
            if backtrack(i, first):
                return True
        
        return False