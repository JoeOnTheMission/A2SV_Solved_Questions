class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = {}
        losers = {}
        for winner, loser in matches:
            winners[winner] = winners.get(winner,0) + 1
            losers[loser] = losers.get(loser,0) + 1

        res = [[],[]]
        for player in winners:
            if player not in losers:
                res[0].append(player)
        for player in losers:
            if losers[player] == 1:
                res[1].append(player)
        res[0].sort()
        res[1].sort()
        return res