from collections import deque

q = int(input())

def one_sulip():
    pass

first_cmd = list(map(int, input().split()))
n, m = first_cmd[1], first_cmd[2]

ids = deque(first_cmd[3:3+n])
weights = deque(first_cmd[3+n:])

belts = list()
for i in range(m):
    belts.append(deque())

for i in range(m):
    for j in range(int(n/m)):
        belts[i].append((ids.popleft(), weights.popleft()))


command = list()
for _ in range(q-1):
    command.append((list(map(int, input().split()))))


result_list = list()

def two_hacha(w_max):
    hacha_sum = 0
    for i in range(m):
        if belts[i]:
            top = belts[i].popleft()
            if top[1] <= w_max:
                hacha_sum+=top[1]
            else:
                belts[i].append(top)
    result_list.append(hacha_sum)

def three_jegu(r_id):
    result=-1
    for i in range(m):
        for box in belts[i]:
            if box[0] == r_id:
                belts[i].remove((box[0], box[1]))
                result_list.append(r_id)
                return
    result_list.append(-1)

def four_hwagin(f_id):
    for i in range(m):
        for box_idx in range(len(belts[i])):
            if belts[i][box_idx][0] == f_id:
                tempq = deque()
                for pop_cnt in range(len(belts[i])-box_idx):
                    tempq.append(belts[i].pop())
                while tempq:
                    belts[i].appendleft(tempq.popleft())

                result_list.append(i+1)
                return
    result_list.append(-1)

def five_gojang(b_num):
    if len(belts[b_num]) == 0:
        result_list.append(-1)
        return

    belt_len = len(belts)
    for i in range(1, belt_len):
        belt_idx = (b_num+i)%belt_len
        if len(belts[belt_idx])>0:
            while belts[b_num]:
                belts[belt_idx].append(belts[b_num].popleft())
            break
    result_list.append(b_num+1)
    # belts.pop(b_num)

for cmd in command:
    if cmd[0] == 200:
        two_hacha(cmd[1])
    elif cmd[0] == 300:
        three_jegu(cmd[1])
    elif cmd[0] == 400:
        four_hwagin(cmd[1])
    elif cmd[0] == 500:
        five_gojang(cmd[1]-1)

    # # debug
    # print(cmd[0], end=": ")
    # for belt in belts:
    #     print(belt)
    # print(result_list[-1])

#FINALLY
# print("!!!FINNALLYYY!!!")
for result in result_list:
    print(result)

