class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        mine = defaultdict(int)
        mine[0] += float("inf")
        for cust in bills:
            #print(cust,mine)
            change = cust - 5
            if change == 0:#given 5
                mine[5] += 1
            elif change == 5:#given 10
                if mine[5] < 1:
                    return False
                else:
                    mine[5] -= 1
                    mine[10] += 1
            elif change == 15:#given 20
                if mine[10] < 1 or mine[5] < 1:
                    if  mine[5] < 3:
                        return False
                    else:
                        mine[5] -= 3
                else:
                    mine[10] -= 1
                    mine[5] -= 1
            #print(mine)
        return True