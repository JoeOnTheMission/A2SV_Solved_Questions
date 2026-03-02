class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        offset = ord("a")
        num_version =[ord(letter) - offset for letter in s]

        prefix = [0]*len(s)
        for l,r,shift in shifts:
            if shift == 1:
                k = 1
            else:
                k = -1

            prefix[l] += k

            if r+1 < len(s):
                prefix[r+1] -= k
    
        for i in range(1,len(prefix)):
            prefix[i] += prefix[i-1]

        for i in range(len(num_version)):
            num_version[i] = (num_version[i] + prefix[i]) % 26

        res = ""
        for num in num_version:
            res += chr(num + offset)
        return res
            
