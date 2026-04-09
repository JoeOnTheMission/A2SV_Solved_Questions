class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        all = []

        def backtrack(comb):
            if len(comb) == n:
                all.append(comb[:])
                return
            
            for letter in ["a","b","c"]:
                if comb and comb[-1] == letter:
                    continue
                comb.append(letter)
                backtrack(comb)
                comb.pop()
        backtrack([])
        all.sort()
        if k-1 < len(all):
            return "".join(all[k-1])
        else:
            return ""
        