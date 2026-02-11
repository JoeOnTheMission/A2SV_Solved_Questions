class Solution:
    def findValidPair(self, s: str) -> str:
        s_counter = Counter(s)
        for i in range(len(s)-1):
            x = s[i]
            y = s[i+1]
            if x == y:
                continue
            else:
                if int(x) == s_counter[x] and int(y) == s_counter[y]:
                    return(x+y)
        else:
            return ""