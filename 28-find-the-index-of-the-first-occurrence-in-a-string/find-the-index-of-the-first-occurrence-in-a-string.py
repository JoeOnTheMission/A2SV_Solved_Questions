class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        done = False
        while not done and i < len(haystack):
            if haystack[i] == needle[j]:
                while j < len(needle) and i < len(haystack) and  haystack[i] == needle[j]:
                    i += 1
                    j += 1
                if j == len(needle):# found
                    done = True
                else:
                    i = i - j + 1
                    j = 0
            else:
                i += 1
        if done:
            return i-len(needle)
        else:
            return -1