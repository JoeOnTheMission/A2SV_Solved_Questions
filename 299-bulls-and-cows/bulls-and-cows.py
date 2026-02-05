class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        seen = {}
        skip = []
        x = 0
        y = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                x += 1
                skip.append(i)
            else:
                seen[secret[i]] = seen.get(secret[i],0) + 1
        skip.append("end")
        skipIndex = 0
        for i in range(len(secret)):
            if i == skip[skipIndex]: #aready matched on the bull
                skipIndex += 1
            elif guess[i] in seen:
                if seen[guess[i]] > 0 :
                    y += 1  
                    seen[guess[i]] -= 1     
        return f"{x}A{y}B"   
            


        