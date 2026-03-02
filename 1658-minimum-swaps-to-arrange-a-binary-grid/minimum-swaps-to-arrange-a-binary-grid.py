class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Step 1: count trailing zeros
        trailing = []
        for row in grid:
            count = 0
            for num in reversed(row):
                if num == 0:
                    count += 1
                else:
                    break
            trailing.append(count)
        
        swaps = 0
        
        # Step 2: greedy positioning
        for i in range(n):
            needed = n - i - 1
            j = i
            
            # find row that satisfies condition
            while j < n and trailing[j] < needed:
                j += 1
            
            if j == n:
                return -1
            
            # move row up
            while j > i:
                trailing[j], trailing[j-1] = trailing[j-1], trailing[j]
                swaps += 1
                j -= 1
        
        return swaps