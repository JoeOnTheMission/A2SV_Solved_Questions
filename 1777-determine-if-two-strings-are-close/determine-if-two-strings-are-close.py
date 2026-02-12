class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        counter_1 = Counter(word1)
        counter_2 = Counter(word2)
        counts_1 = sorted(list(counter_1.values()))
        counts_2 = sorted(list(counter_2.values()))
        if counts_1 != counts_2:
            return False
        for letter in counter_1:
            if letter not in counter_2:
                return False
        return True