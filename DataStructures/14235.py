import heapq
n = int(input())

gift = list()

result = list()
for _ in range(n):
    a = list(map(int, input().split()))
    # print(a)
    if a[0] == 0:
        if len(gift)==0:
            result.append(-1)
        else:
            result.append(-heapq.heappop(gift))
    else:
        for a_elem in a[1:]:
            heapq.heappush(gift, -a_elem)

for r in result:
    print(r)