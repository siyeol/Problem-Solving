board = [[0]*101 for _ in range(101)]

def get_dragon (gen, dir):
    dragon_gen = list()
    if dir == 0:
        dragon_gen.append([[0,1]])
    elif dir == 1:
        dragon_gen.append([[-1,0]])
    elif dir == 2:
        dragon_gen.append([[0,-1]])
    elif dir == 3:
        dragon_gen.append([[1,0]])

    for i in range(1, gen+1):
        temp_list = dragon_gen[i-1]
        for dg in dragon_gen[i-1][::-1]:
            y, x = dg
            temp_list.append([-x, y])
        dragon_gen.append(temp_list)

    return dragon_gen[-1]

N = int(input())
for _ in range(N):
    x, y, d, g = map(int, input().split())
    dragon_list = get_dragon(g, d)
    board[y][x]=1

    for dragon in dragon_list:
        y+=dragon[0]
        x+=dragon[1]
        board[y][x] = 1

result_cnt = 0
for y in range(100): #끝 주의
    for x in range(100):
        if board[y][x] == 1 and board[y+1][x] == 1 and board[y][x+1] == 1 and board[y+1][x+1] == 1:
            result_cnt+=1

print(result_cnt)
