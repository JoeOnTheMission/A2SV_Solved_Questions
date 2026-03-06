class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        i = 0
        subarray_count = 0
        while i < len(s):
            if s[i] == "1":
                subarray_count += 1
                while i < len(s) and s[i] == "1":
                    i += 1 
            i += 1
        if subarray_count < 2:
            return True
        else:
            return False