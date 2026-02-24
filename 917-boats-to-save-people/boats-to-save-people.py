class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = len(people) - 1
        valid_pair = 0
        while i < j:
            weight = people[i] + people[j]
            if weight > limit:
                j -= 1 
            else:#can be a boat
                valid_pair += 1
                i += 1
                j -= 1
        return len(people) - valid_pair