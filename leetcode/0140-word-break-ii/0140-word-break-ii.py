class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        min_word = len(wordDict[0])
        max_word = len(wordDict[0])
        for word in wordDict:
            min_word = min(min_word,len(word))
            max_word = max(max_word,len(word)) 
        #print(max_word)

        res = []
        now = []
        def backtrack(start):
            #print(start,now)
            if start >= len(s):
                res.append(" ".join(now))
            #find word
            word = ""
            #print(start,range(start,start + max_word))
            for i in range(start,start + max_word + 1):
                
                if i >= len(s):
                    #print("here")
                    break
                word += s[i]
                #print(start,word)
                if word in wordDict:
                    now.append(word)
                    backtrack(i+1)
                    now.pop()

        backtrack(0)
        return res