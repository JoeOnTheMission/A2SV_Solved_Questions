class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ppl = [0]*k
        self.res = float(inf)
        cookies.sort(reverse=True)
        def backtrack(index):
            if index >= len(cookies):
                self.res = min(self.res,max(ppl)) 
                #print(ppl)
                return
            
            for i in range(k):
                #we are trying to minimize so skip this 
                if ppl[i] + cookies[index] >= self.res:
                    continue
                #no point am going to get the same val
                if i > 0 and ppl[i] == ppl[i - 1]:
                    continue

                ppl[i] += cookies[index]
                backtrack(index + 1)
                ppl[i] -= cookies[index]

                #i check this in the first run 
                if ppl[i] == 0:
                    break
        backtrack(0)
        return self.res
