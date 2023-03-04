N = int(input())

arr = list(map(int, input().split()))

dp = [0] * (len(arr)+1)
dp[0] = 1

answer = 1
for i in range(1, N):
    cur_max = 0
    for j in range(i):
        if arr[j] < arr[i]:
            cur_max = max(cur_max, dp[j])
    dp[i] = cur_max+1
    answer = max(answer, dp[i])

print(answer)