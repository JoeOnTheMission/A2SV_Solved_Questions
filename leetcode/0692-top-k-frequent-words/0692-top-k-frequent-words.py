class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        h = []
        for word in counts:
            heapq.heappush(h,(-counts[word],word))
            # if len(h) > k:
            #     heapq.heappop(h)
        res = []
        for i in range(k):
            res.append(heapq.heappop(h)[1])
        return res