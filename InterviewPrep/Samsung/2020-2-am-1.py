from collections import deque

n, k = map(int, input().split())

temp_platform = map(int, input().split())
safety = deque(temp_platform)

testers=deque([0]*n)


def rotate():
    safety.rotate(1)
    testers.rotate(1)

    if testers[-1] == 1:
        testers[-1] = 0

def walk():
    for i in range(n-2, -1, -1):
        if testers[i]==1:
            if testers[i+1] == 0 and safety[i+1]!=0:
                testers[i]=0
                testers[i+1]=1
                safety[i+1]-=1

    if testers[-1] == 1:
        testers[-1] = 0

def putin():
    if testers[0]==0 and safety[0]!=0:
        testers[0] = 1
        safety[0] -= 1

def play():
    cnt = 0
    while safety.count(0)<k:
        rotate()
        walk()
        putin()
        cnt += 1
    return cnt

print(play())
