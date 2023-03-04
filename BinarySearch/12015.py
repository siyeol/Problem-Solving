N = int(input())

arr = list(map(int, input().split()))

prev = 0

cnt = 0
for i in range(N):
    if prev < arr[i]:
        prev = arr[i]
        cnt+=1

print(cnt)