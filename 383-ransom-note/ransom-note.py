class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_counter = Counter(ransomNote)
        m_counter = Counter(magazine)
        for letter in r_counter:
            if letter in m_counter:
                if r_counter[letter] > m_counter[letter]:
                    return False
            else:
                return False
        else:
            return True