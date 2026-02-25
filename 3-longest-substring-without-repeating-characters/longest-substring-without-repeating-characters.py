class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_window_size = 0
        left = 0
        right = 0
        window_letters = set()
        while right < len(s):
            letter = s[right]
            if letter in window_letters:
                while letter in window_letters:
                    window_letters.remove(s[left])
                    left += 1
            if letter not in window_letters:
                window_letters.add(letter)
                right += 1
                max_window_size = max(max_window_size,right-left)
        return max_window_size