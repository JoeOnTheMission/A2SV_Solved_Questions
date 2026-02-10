class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s = list(s)
    
        combined = zip(indices,s)
        res = sorted(combined)
        key,soln = zip(*res)
        return "".join(soln)

