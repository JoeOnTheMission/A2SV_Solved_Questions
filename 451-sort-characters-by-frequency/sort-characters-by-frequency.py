class Solution:
    def frequencySort(self, s: str) -> str:
        s_counter = Counter(s)
        res = sorted(s,key=lambda letter:(-s_counter[letter],letter))
        return "".join(res)