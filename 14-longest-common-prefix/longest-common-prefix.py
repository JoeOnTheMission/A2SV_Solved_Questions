class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        result = ""
        for i in range(min(len(strs[0]),len(strs[-1]))):
            if strs[0][i] == strs[-1][i]:
                result += strs[0][i]
            else:
                break
        return result