class Solution:
    def smallestPalindrome(self, s: str) -> str:
        d = Counter(s)
        sub = []
        mid = ""
        for letter in d:
        
            if d[letter] % 2 == 0:
                sub.append(letter*(d[letter]//2))
            else:
                mid+= letter
                sub.append(letter*(d[letter]//2))
        sub = sorted(sub)
        res = "".join(sub) + mid + "".join(reversed(sub))
        return res