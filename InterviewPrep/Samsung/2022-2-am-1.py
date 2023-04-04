# def solution():

n, m, k = map(int, input().split())

board = [[[] for _ in range(n)] for _ in range(n)]
for y in range(n):
    temp_list = list(map(int, input().split()))
    for x in range(n):
        board[y][x].append(temp_list[x])

# 위 오른 아래 왼
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

players = list()
for _ in range(m):
    y, x, d, s = map(int, input().split())
    players.append([y - 1, x - 1, d, s, 0, 0])


def win_play(idx, diff_point):
    players[idx][4] += diff_point
    (y, x, d, s, point, gun) = players[idx]
    if sum(board[y][x]) > 0:
        # compare values
        mg = max(board[y][x])
        if gun < mg:
            board[y][x].append(gun)
            players[idx][5] = mg
            board[y][x].remove(mg)


def lose_play(idx):
    # print(players[idx])
    (y, x, d, s, point, gun) = players[idx]
    board[y][x].append(gun)
    players[idx][-1] = 0
    gun = 0

    for i in range(4):
        dd = (d+i)%4
        yy = y+dy[dd]
        xx=x+dx[dd]

        if (0<=yy<n) and (0<=xx<n):
            player_flag = False
            for pi, player in enumerate(players):
                if player[0] == yy and player[1] == xx and pi != idx:
                    player_flag = True
            if player_flag is False:
                if sum(board[yy][xx]) > 0:
                    # compare values
                    mg = max(board[yy][xx])
                    players[idx][5] = mg
                    board[yy][xx].remove(mg)
                players[idx][0], players[idx][1], players[idx][2] = yy, xx, dd
                return

def move():
    for idx in range(m):
        (y, x, d, s, point, gun) = players[idx]
        yy = y + dy[d]
        xx = x + dx[d]

        # 1-1
        if not (0 <= yy < n) or not (0 <= xx < n):
            d = (d + 2) % 4
            yy = y + dy[d]
            xx = x + dx[d]

        # UPDATE #여기 매우매우 중요!!
        players[idx] = [yy, xx, d, s, point, gun]

        # 2-1
        opponent = -1
        for i in range(m):
            if players[i][0] == yy and players[i][1] == xx and idx != i:
                opponent = i
                break

        if opponent == -1:
            if sum(board[yy][xx]) > 0:
                # compare values
                max_gun = max(board[yy][xx])
                if gun < max_gun:
                    if gun != 0:
                        board[yy][xx].append(gun)
                    players[idx][5] = max_gun
                    board[yy][xx].remove(max_gun)

        # 2-2-1
        else:
            cur_player = s + gun

            (opy, opx, opd, ops, oppoint, opgun) = players[opponent]
            oppo_player = ops + opgun

            diff_point = abs(cur_player - oppo_player)
            winnder_idx, loser_idx = 0, 0
            if cur_player == oppo_player:
                if s > ops:  # cur win
                    winnder_idx = idx
                    loser_idx = opponent
                else:  # oppo win
                    winnder_idx = opponent
                    loser_idx = idx
            elif cur_player > oppo_player:  # cur win
                winnder_idx = idx
                loser_idx = opponent
            else:
                winnder_idx = opponent  # oppo win
                loser_idx = idx

            lose_play(loser_idx)
            win_play(winnder_idx, diff_point)

#MAIN
for _ in range(k):
    move()

answer = ""
for player in players:
    answer = answer+str(player[4])+" "

answer.rsplit()
print(answer)