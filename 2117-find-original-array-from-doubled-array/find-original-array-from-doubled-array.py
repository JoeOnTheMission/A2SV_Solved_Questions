class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        seen = defaultdict(int)
        original = []
        for num in changed:
            if num % 2 == 0:
                if num // 2 in seen:
                    seen[num // 2] -= 1
                    if seen[num // 2] == 0:
                        seen.pop(num // 2)
                    original.append(num // 2)
                else:
                    seen[num] += 1
            else:#must be in original
                seen[num] += 1

        return original if len(changed) == len(original)*2 else []