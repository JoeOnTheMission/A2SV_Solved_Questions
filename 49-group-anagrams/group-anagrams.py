class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        d = defaultdict(list)

        for i in range(len(strs)):
            word = strs[i]
            k = "".join(sorted(word))
            d[k].append(word)
        res = []
        for l in d:
            res.append(d[l])
        return res