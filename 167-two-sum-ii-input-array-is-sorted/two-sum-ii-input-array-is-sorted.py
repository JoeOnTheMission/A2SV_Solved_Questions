class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        found = False
        i = 0
        j = len(numbers)-1
        while not found:
            if numbers[i] + numbers[j] == target:
                found = True
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1
        return [i + 1, j + 1 ]