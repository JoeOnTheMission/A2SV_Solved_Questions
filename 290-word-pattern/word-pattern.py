class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(" ")
        s_set  = set(s_list)#all unique words 
        checker = defaultdict(list)
        u_letters = 0
        if len(pattern) != len(s_list):
            return False
        for i in range(len(pattern)):
            letter = pattern[i]
            word = s_list[i]
            
            if letter in checker:
                if checker[letter][0] != word:
                    return False
                    break
            else:
                checker[letter].append(word)
                u_letters += 1
        else:
            
            if u_letters != len(s_set):
                return False  
            else:
                return True