from collections import deque

def solution(people, limit):
    answer = 0
    
    dq = deque(sorted(people))
    
    left = 0
    right = len(dq)-1
    
    cnt = 0
    while True:
        if dq[0]+dq[-1] > limit:
            dq.pop()
            cnt+=1    
        else:
            dq.popleft()
            dq.pop()
            cnt+=1
            
        if len(dq) == 0:
            break
        elif len(dq) == 1:
            cnt+=1
            break
    
    return cnt
        