class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counter = Counter(nums)
        res = sorted(nums_counter.keys(),key=lambda x : nums_counter[x],reverse=True)
        return res[:k]
