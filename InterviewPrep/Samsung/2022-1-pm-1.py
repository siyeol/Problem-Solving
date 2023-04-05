from collections import deque

n, m, k = map(int, input().split())

board = list()
for _ in range(n):
    board.append(list(map(int, input().split())))

team = list()
for _ in range(m):
    team.append(deque())

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

def trace_back(y, x, team_no):
    if board[y][x] == 3:
        return

    for i in range(4):
        yy = y+dy[i]
        xx = x+dx[i]

        if 0<=yy<n and 0<=xx<n and not visited[yy][xx]:
            if board[yy][xx]==board[y][x]+1 or board[yy][xx]==board[y][x]:
                visited[yy][xx]=1
                team[team_no].append([yy, xx])
                trace_back(yy, xx, team_no)
                visited[yy][xx]=0

team_no = 0
for y in range(n):
    for x in range(n):
        if board[y][x] == 1:
            visited = [[0]*n for _ in range(n)]
            visited[y][x] = 1
            team[team_no].append([y, x])
            trace_back(y, x, team_no)
            team_no+=1

# def turn():
def move_team():
    for team_no in range(m):
        last = team[team_no].pop()
        board[last[0]][last[1]] = 4
        new_last = team[team_no][-1]
        board[new_last[0]][new_last[1]] = 3

        head = team[team_no][0]
        board[head[0]][head[1]] = 2
        for i in range(4):
            yy = head[0]+dy[i]
            xx = head[1]+dx[i]

            if 0<=yy<n and 0<=xx<n and board[yy][xx] == 4:
                team[team_no].appendleft([yy, xx])
                board[yy][xx] = 1
                break

answer = 0

def get_point(y,x):
    # print(y, x, "HEREYOU GET")
    global answer
    for tm_no, tm in enumerate(team):
        for idx, person in enumerate(tm):
            if [y,x] == person:
                answer+=(idx+1)**2

                team[tm_no].reverse()

                new_head=team[tm_no][0]
                new_tail = team[tm_no][-1]

                board[new_head[0]][new_head[1]] = 1
                board[new_tail[0]][new_tail[1]] = 3

                return

rounds = list()
for i in range(4*n):
    rounds.append(list())

round_idx = 0
for y in range(n):
    for x in range(n):
        rounds[round_idx].append((y, x))
    round_idx+=1
for x in range(n):
    for y in range(n-1, -1, -1):
        rounds[round_idx].append((y, x))
    round_idx += 1

for y in range(n-1, -1, -1):
    for x in range(n-1, -1, -1):
        rounds[round_idx].append((y, x))
    round_idx += 1

for x in range(n-1, -1, -1):
    for y in range(n):
        rounds[round_idx].append((y, x))
    round_idx += 1


def throw_ball(turn):
    turn = turn % (4 * n)
    cur_round = rounds[turn]

    for cury, curx in cur_round:
        if 1 <= board[cury][curx] <= 3:
            get_point(cury, curx)
            return

for turn in range(k):
    move_team()
    throw_ball(turn)

print(answer)
