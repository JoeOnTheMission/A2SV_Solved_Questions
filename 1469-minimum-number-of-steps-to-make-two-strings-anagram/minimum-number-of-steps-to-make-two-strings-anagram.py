class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_counter = Counter(s)
        t_counter = Counter(t)
        res = 0
        for s in s_counter:
            if s in t_counter:
                if t_counter[s] < s_counter[s]:
                    res += s_counter[s] - t_counter[s] 
            else:
                res += s_counter[s]
        return res