class Solution:
    def smallestNumber(self, pattern: str) -> str:
        now = []
        n = len(pattern)
        res = []
        def backtrack(index):
            if len(now) == n+1:
                print("here")
                res.append(now[:])
                return 
            if len(res)!= 0:
                return
            if pattern[index] == "I":
                for i in range(now[-1]+1,10):
                    if i in now:
                        continue
                    now.append(i)
                    backtrack(index + 1)
                    now.pop()
            else:
                for j in range(1,now[-1]):
                    if j in now:
                        continue
                    now.append(j)
                    backtrack(index + 1)
                    now.pop()
        for k in range(1,10):
            now.append(k)
            backtrack(0)
            now.pop()
            if len(res) != 0:
                break
        return "".join([str(x) for x in res[0]])