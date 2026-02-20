class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = {}
        i = 0
        for letter in order:
            d[letter] = i
            i += 1
        def checker(letter):
            if letter in d:
                return d[letter]
            else:
                return ord(letter)
        res = sorted(s,key=lambda letter : checker(letter))
        return "".join(res)