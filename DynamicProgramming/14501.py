from math import inf
N = int(input())
schedule=list()

for _ in range(N):
    T, P = map(int, input().split())
    schedule.append((T, P))

dp = [0] * (N+1)

for i in range(N-1, -1, -1):
    if schedule[i][0]+i>N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[schedule[i][0]+i]+schedule[i][1])

print(dp[0])