class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d = {}
        res = 0
        for letter in chars:
            d[letter] = d.get(letter,0) + 1
        for word in words:
            checker = {}
            for letter in word:
                if letter not in d:
                    break
                else:
                    checker[letter] = checker.get(letter,0) + 1
            else:
                for letter in checker:
                    count = checker[letter]
                    if count > d[letter]:#can't make word
                        break
                else:
                    res += len(word)
        return res