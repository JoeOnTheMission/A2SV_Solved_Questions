class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pre = [0]*(len(s)+1)
        for l,r,d in shifts:
            if d == 1:
                pre[l] += 1
                pre[r+1] -= 1
            else:
                pre[l] -= 1
                pre[r+1] += 1
        for i in range(1,len(pre)):
            pre[i] += pre[i-1]
        res = []
        for i,letter in enumerate(s):
            offset = ord("a")
            new_letter = chr(((ord(letter) - offset + pre[i]) % 26) + offset)
            res.append(new_letter)
        return "".join(res)