N = int(input())

stair = [0]*(N+1)

for i in range(N):
    stair[i+1] = int(input())

dp = [0]*(N+1)

if N>=3:

    dp[0] = 0
    dp[1] = stair[1]
    dp[2] = stair[1]+stair[2]

    for i in range(3, N+1):
        dp[i] = max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])

    print(dp[-1])

elif N == 1:
    print(stair[1])
elif N == 2:
    print(stair[1]+stair[2])