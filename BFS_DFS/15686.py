from collections import deque
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

# from itertools import combinations
# chicken_perm = combinations(chicken, M)

l = chicken
n = len(chicken)
r = M
chicken_perm = []

def get_combi(idx, list):
    if len(list) == r:
        chicken_perm.append(list[:])
        return

    for i in range(idx, n):
        get_combi(i+1,list+[l[i]])

get_combi(0, [])

def dist(home, chicken):
    return abs(home[0]-chicken[0]) + abs(home[1]-chicken[1])

min_dist = inf

from collections import deque
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

visited=[[0]*N for _ in range(N)]
def BFS(y, x, chickp):
    q = deque()
    q.append((y, x))
    visited[y][x] = 1

    while q:
        cury, curx = q.popleft()
        if (cury, curx) in chickp:
            return dist([yy,xx], chick)

        for i in range(4):
            yy = cury+dy[i]
            xx = curx+dx[i]
            if 0<=yy<N and 0<=xx<N and not visited[yy][xx]:
                visited[yy][xx] = 1
                q.append((yy,xx))

for chickp in chicken_perm:
    dist_total = 0
    # print(chickp, type(chickp))
    for house in houses:
        # print(house, type(house))
        closest_chick = inf
        for chick in chickp:
            closest_chick = min(closest_chick, dist(house, chick))
        dist_total+=closest_chick
        if dist_total>=min_dist:
            break
    min_dist = min(min_dist, dist_total)

print(min_dist)