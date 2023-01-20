import heapq

n = int(input())

rails = []
for _ in range(n):
    small, large = sorted(list(map(int, input().split())))
    rails.append([small, large])

d = int(input())

rails = [[s, l] for s, l in rails if l-s<=d]
rails.sort(key= lambda x:x[1])

result = 0
hq = []

for rail in rails:
    if not hq :
        heapq.heappush(hq, rail)
    else:
        while hq[0][0] < rail[1] - d:
            heapq.heappop(hq)
            if len(hq):
                break
        heapq.heappush(hq, rail)
    result = max(result, len(hq))

print(result)