import heapq

N = int(input())

left_hq = []
right_hq = []

result = []

for _ in range(N):
    num = int(input())

    if len(left_hq)==len(right_hq):
        heapq.heappush(left_hq, -num)
    else:
        heapq.heappush(right_hq, num)

    if len(right_hq) and -left_hq[0] > right_hq[0]:
        lpop = heapq.heappop(left_hq)
        rpop = heapq.heappop(right_hq)

        heapq.heappush(right_hq, -lpop)
        heapq.heappush(left_hq, -rpop)
        
    result.append(-left_hq[0])
        
for r in result:
    print(r)