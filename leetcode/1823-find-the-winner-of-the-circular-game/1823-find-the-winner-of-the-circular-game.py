class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = list(range(1,n+1))
        now = 0
        while len(arr) > 1:
            remove_index = (now + k -1 )% len(arr)
            arr.pop(remove_index)
            now = remove_index
        return arr[0]