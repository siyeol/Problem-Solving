from collections import deque
def solution(cap, n, deliveries, pickups):
    dq = deque()
    pq = deque()
    
    for i in range(n):
        if deliveries[i] != 0:
            dq.append([i,deliveries[i]])
        if pickups[i] != 0:
            pq.append([i, pickups[i]])

    distance = 0
    def pickup(distance):
        d_cap = cap
        p_cap = cap

        if dq and pq:
            curmax = max(dq[-1][0], pq[-1][0])
        elif dq and not pq:
            curmax = dq[-1][0]
        elif not dq and pq:
            curmax = pq[-1][0]

        distance += 2*(curmax+1)

        for i in range(len(dq)-1, -1, -1):
            if d_cap >= dq[i][1]:
                d_cap -= dq[i][1]
                dq.pop()
                
            elif dq[i][1]-d_cap>0:                
                dq[i][1]-=d_cap
                d_cap = 0
                break

        for i in range(len(pq)-1, -1, -1):
            if p_cap >= pq[i][1]:
                p_cap -= pq[i][1]
                pq.pop()
                
            elif pq[i][1]-p_cap>0:                
                pq[i][1]-=p_cap
                p_cap = 0
                break
        
        return distance
            
    # print(dq)
    # print(pq)
    while True:
        if len(dq) == 0 and len(pq)==0:
            break
        distance = pickup(distance)
        # print(dq)
        # print(pq)

    # print("ANS", distance)
    return distance

cap = 2
n = 7
deliveries = [1, 0, 2, 0, 1, 0, 2]	
pickups = [0, 2, 0, 1, 0, 2, 0]

cap = 4
n = 5
deliveries = [1, 0, 3, 1, 2]	
pickups = [0, 3, 0, 4, 0]


solution(cap, n, deliveries, pickups)