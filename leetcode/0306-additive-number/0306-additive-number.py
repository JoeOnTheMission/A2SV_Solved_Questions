class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        if n < 3:
            return False

        def backtrack(last1, last2, start):
            if start == n:
                return True

            for length in range(1, n - start + 1):
    
                if num[start] == '0' and length > 1:
                    break

                now = int(num[start:start+length])
                running = last1 + last2

                if now < running:
                    continue
                elif now > running:
                    break
                else:
                    if backtrack(last2, now, start + length):
                        return True

            return False

        for i in range(n - 2):
            for j in range(i + 1, n - 1):

                if num[0] == '0' and i > 0:
                    break
                if num[i + 1] == '0' and j > i + 1:
                    break

                first = int(num[:i+1])
                second = int(num[i+1:j+1])

                if backtrack(first, second, j + 1):
                    return True

        return False