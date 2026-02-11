class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M',
             4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}

        base = len(str(num))-1
        base2 = len(str(num))-1
        digits = [int(x) for x in str(num)]
        """while num >= 10:#separate in to digits 
            left = (num // (10**base)) 
            digits.append(left)
            num = num % (10**base)
            base -= 1
        digits.append(num)"""
        res = []
        for digit in digits:
            if digit == 0:
                base2 -= 1
                continue
            elif digit in {2,3}:
                while digit > 0:
            
                    digit = ((digit*(10**base2)) - (10**base2))//(10**base2)
                    res.append( d[10**base2] )

                print(digit,res)
            elif digit in {1,4,5,9,10}:
                res.append(d[digit*(10**base2)])
            else:#{6,7,8}
                digit = digit - 5
                res.append(d[5*(10**base2)])#the left
                while digit > 0:

                    digit = ((digit*(10**base2)) - (10**base2))//(10**base2)
                    res.append( d[10**base2] )
            base2 -= 1
        return "".join(res)
                    