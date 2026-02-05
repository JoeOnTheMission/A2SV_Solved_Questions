class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        needed = set(range(left,right+1))
        have = set()
        for start, end in ranges:
            l = [x for x in range(start,end+1)]
            have.update(l)
        if needed.issubset(have):
            return True
        else:
            return False
