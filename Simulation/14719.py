H, W = map(int, input().split())

box = [[0]*W for _ in range(H+1)]

rain = list(map(int, input().split()))
for idx, r in enumerate(rain):
    for h in range(r, -1, -1):
        box[h][idx]=1


result = 0
for y in range(1, H+1):
    isStart = False
    temp = 0
    for horiz in range(W-1):
        cur = box[y][horiz]
        next = box[y][horiz+1]
            
        if cur == 1 and isStart is False:
            isStart = True
            if sum(box[y][horiz+1:]) == 0:
                isStart = False
        elif cur == 1 and isStart is True and next == 0:
            isStart = True
        elif cur == 1 and isStart is True and next == 1:
            isStart = False
        elif cur == 0 and isStart is True:
            result += 1
        elif cur == 0 and isStart is False:
            continue

print(result)