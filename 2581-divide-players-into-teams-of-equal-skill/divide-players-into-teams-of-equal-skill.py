class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        team_skill = skill[0] + skill[-1]
        res = []
        for i in range(len(skill)//2):
            if skill[i] + skill[len(skill) - i - 1] != team_skill:
                break
            else:
                res.append(skill[i] * skill[len(skill) - i - 1])
        else:
            return sum(res)
        return -1