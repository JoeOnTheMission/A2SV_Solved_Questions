class Solution:
    def checkEqual(self, a, b) -> bool:
        if len(a) != len(b):
            return False
        a.sort()
        b.sort()
        i = 0
        j = 0
        while i < len(a):
            if a[i] != b[j]:
                return False
            i+=1
            j+=1
        return True
            
