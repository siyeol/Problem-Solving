import heapq

N = int(input())

num = list()
for _ in range(N):
    heapq.heappush(num, int(input()))

sum = 0
while len(num)>1:
    temp1 = heapq.heappop(num)
    temp2 = heapq.heappop(num)
    sum+=(temp1+temp2)
    heapq.heappush(num, temp1+temp2)


print(sum)
