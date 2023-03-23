from collections import deque
from copy import deepcopy
from math import inf
N, M = map(int, input().split())

board = list()
chicken = list()
houses = list()
for y in range(N):
    temp_list = list(map(int, input().split()))
    for x in range(len(temp_list)):
        if temp_list[x] == 2:
            chicken.append((y, x))
        if temp_list[x] == 1:
            houses.append((y, x))
    board.append(temp_list)

chicken_perm = list()
def perm(cnt, stack):
    if cnt == M:
        if stack not in chicken_perm:
            chicken_perm.append(stack)        
        return
    
    for i in range(cnt, len(chicken)):
        if chicken[i] not in stack:
            temp_stack = deepcopy(stack)
            temp_stack.add(chicken[i])
            perm(cnt+1, temp_stack)
            # temp_stack.pop()

perm(0, set())

def dist(home, chicken):
    return abs(home[0]-chicken[0]) + abs(home[1]-chicken[1])

min_dist = inf

for chickp in chicken_perm:
    dist_total = 0
    for house in houses:
        closest_chick = inf
        for chick in chickp:
            closest_chick = min(closest_chick, dist(house, chick))
        dist_total+=closest_chick
    min_dist = min(min_dist, dist_total)

print(min_dist)