class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {}
        shortest = list1 if len(list1) < len(list2) else list2
        longer = list2 if len(list1) < len(list2) else list1
        res = None
        for i,word in enumerate(shortest):
            d[word] = i
        for i,word in enumerate(longer):
            if word in d:
                value = i + d[word]
                if res == None:# first common found 
                    res = [[word],value]
                else:
                    if res[1] == value: # same value
                        res[0].append(word)
                    elif res[1] > value: # new smaller found
                        res = [[word],value]
        return res[0]