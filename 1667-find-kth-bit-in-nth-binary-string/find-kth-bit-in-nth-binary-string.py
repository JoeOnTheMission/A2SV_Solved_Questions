class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        for i in range(1,n):
            a = [s+"1"]
            inv = ["0" if num == "1" else "1" for num in s ]
            a.extend(reversed(inv))
            s = "".join(a)   
        return s[k-1]