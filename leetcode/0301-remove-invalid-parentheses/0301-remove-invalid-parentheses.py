class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.res = []
        self.cur = []
        self.stack = []
        self.n = len(s)
        self.last_remove_count = float("inf")

        def backtrack(index,remove_count):
            #print("index",index,"remove_count",remove_count)
            if index >= self.n:#base case
                #print(self.res,self.cur)
                if not self.stack:#valid cur
                    if self.last_remove_count == remove_count:
                        self.res.append("".join(self.cur[:]))
                    elif self.last_remove_count > remove_count:
                        self.res = ["".join(self.cur[:])]
                        self.last_remove_count = remove_count
                
                return
            if s[index] == "(":
                #try removing it
                backtrack(index + 1, remove_count + 1)

                #try adding it 
                self.stack.append("(")
                self.cur.append("(")
                backtrack(index + 1,remove_count)
                self.stack.pop()
                self.cur.pop()
                

            elif s[index] == ")":
                #try removing it
                backtrack(index + 1,remove_count + 1)

                #try adding it if possible
                if self.stack:
                    self.stack.pop()#it formed a pair
                    self.cur.append(")")
                    backtrack(index + 1,remove_count)
                    self.stack.append("(")
                    self.cur.pop()
            else:
                self.cur.append(s[index])
                backtrack(index + 1,remove_count)
                self.cur.pop()

            
        backtrack(0,0)
        res2 = []
        seen = set()
        for ans in self.res:
            if ans in seen:
                continue
            else:
                seen.add(ans)
                res2.append(ans)

            
        return res2