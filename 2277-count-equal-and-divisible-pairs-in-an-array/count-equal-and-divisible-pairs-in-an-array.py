class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        storage = defaultdict(list)
        res = 0 
        for i in range(len(nums)):
            storage[nums[i]].append(i)
        for num in storage:
            l = len(storage[num])
            i = 0
            while i < len(storage[num]):
                index_list = sorted(storage[num],key = lambda index : index % k)
                index = index_list[i]
                l -= 1#remove current num
                if index % k == 0:
                    res += l
                else:
                    possible  = index_list[i+1:]
                    x = index
                    for y in possible:
                        if x*y % k == 0:
                            res += 1
                i += 1
        return res