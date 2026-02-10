class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        storage = defaultdict(list)
        for word in strs:
            key = str(sorted(word))
            storage[key].append(word)
        res = []
        for key in storage:
            res.append(storage[key])
        return res