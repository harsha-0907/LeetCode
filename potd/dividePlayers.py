# Divide the 'n' players into n//2 teams such that the teams have same total skill
def dividePlayers(skill):
    skill[:] = sorted(skill)
    n = len(skill); total = skill[0] + skill[-1]; mul = 0
    for i in range(n//2):
        tot = skill[i] + skill[n-i-1]
        if tot != total:
            return -1
        mul += (skill[i] * skill[n-i-1])
    return mul