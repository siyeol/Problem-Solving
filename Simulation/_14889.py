from math import inf, factorial
from itertools import combinations

N = int(input())

arr = list()
for _ in range(N):
    arr.append(list(map(int, input().split())))

people = [i for i in range(N)]
visited = [0]*N

total = 0
for a in arr:
    total += sum(a)

comb_result = set()
def my_combi(arr, cnt):
    for elem in arr:
        pass

def get_team_sum(team):
    teamsum = 0
    for y, x in combinations(team, 2):
        teamsum+=(arr[y][x]+arr[x][y])
        
    return teamsum

def get_opponent(team):
    other = list()
    for player in people:
        if player not in team:
            other.append(player)

    return other

min_diff=inf
for comb in combinations(people, int(N/2)):
    diff = abs(get_team_sum(comb) - get_team_sum(get_opponent(comb)))
    min_diff = min(min_diff, diff)

print(min_diff)