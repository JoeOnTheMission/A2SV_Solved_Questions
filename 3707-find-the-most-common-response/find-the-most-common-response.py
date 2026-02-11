class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        response_counter = defaultdict(int)
        for day in responses:
            seen = set()
            for response in day:
                if response not in seen:# only unique responses per day get in 
                    seen.add(response)
                    response_counter[response] += 1
        sorted_version = sorted(response_counter.items(),key=lambda item: (-item[1],item[0]))
        return sorted_version[0][0]