from collections import deque


t1 = deque(list(input()))
t2 = deque(list(input()))
t3 = deque(list(input()))
t4 = deque(list(input()))

K=int(input())

cmd = list()
for _ in range(K):
    cmd.append(list(map(int, input().split())))

idx_list = [0, 1, 2, 3]

def turn(wheel, dir):
    if dir == 1:
        endval = wheel.pop()
        wheel.appendleft(endval)
    else:
        startval = wheel.popleft()
        wheel.append(startval)
    return wheel

#위 오른 아래 왼
#N = 0, S = 1
#1 +1  -1 -1
# 오른쪽 = idx 2 // 왼쪽 = idx -2

# check_list = [False, False, False]
#True 돌려 // Flase 안돌려

def check():
    check_list = [False, False, False]
    if t1[2] != t2[-2]:
        check_list[0] = True
    if t2[2] != t3[-2]:
        check_list[1] = True
    if t3[2] != t4[-2]:
        check_list[2] = True
    return check_list

# print(check_list)
for idx, dir in cmd:
    check_list = check()

    if idx == 1:
        t1 = turn(t1, dir)
        if check_list[0]:
            t2 = turn(t2, -dir)
            if check_list[1]:
                t3 = turn(t3, dir)
                if check_list[2]:
                    t4 = turn(t4, -dir)    
    elif idx == 2:
        t2 = turn(t2, dir)
        if check_list[0]:
            t1 = turn(t1, -dir)
        if check_list[1]:
            t3 = turn(t3, -dir)
            if check_list[2]:
                t4 = turn(t4, dir)
    elif idx == 3:
        t3 = turn(t3, dir)
        if check_list[2]:
            t4 = turn(t4, -dir)
        if check_list[1]:
            t2 = turn(t2, -dir)
            if check_list[0]:
                t1 = turn(t1, dir)
    else:
        t4 = turn(t4, dir)
        if check_list[2]:
            t3 = turn(t3, -dir)
            if check_list[1]:
                t2 = turn(t2, dir)
                if check_list[0]:
                    t1 = turn(t1, -dir)

score = 0
if t1[0] == '1':
    score+=1
if t2[0] == '1':
    score+=2
if t3[0] == '1':
    score+=4
if t4[0] == '1':
    score+=8

print(score)