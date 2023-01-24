first = input()
second = input()

flen = len(first)+1
slen = len(second)+1
dp = [[0]*(flen) for _ in range(slen)]

result = ""

for f in range(1, flen):
    for s in range(1, slen):
        if first[f-1] == second[s-1]:
            dp[s][f] = dp[s-1][f-1]+1
        else:
            dp[s][f] = max(dp[s-1][f], dp[s][f-1])

print(dp[-1][-1])