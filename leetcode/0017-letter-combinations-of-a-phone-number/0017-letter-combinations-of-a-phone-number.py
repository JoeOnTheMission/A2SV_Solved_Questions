class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        res = []
        phone = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"}
        def backtrack(index,comb):
            #print(index,comb)
            if len(comb) == n:
                res.append("".join(comb[:]))
                return
            if index >= n:
                return
            #add to the comb
            for letter in phone[digits[index]]:
                comb.append(letter)
                backtrack(index + 1,comb)
                comb.pop()
        backtrack(0,[])
        return res