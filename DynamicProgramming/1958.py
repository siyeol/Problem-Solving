first = input()
second = input()
third = input()

flen = len(first)+1
slen = len(second)+1
tlen = len(third)+1

dp = [[[0]*(flen) for _ in range(slen)] for _ in range(tlen)]

for f in range(1, flen):
    for s in range(1, slen):
        for t in range(1, tlen):
            if first[f-1] == second[s-1] and second[s-1] == third[t-1]:
                dp[t][s][f] = dp[t-1][s-1][f-1]+1
            else:
                dp[t][s][f] = max(dp[t-1][s][f], dp[t][s-1][f], dp[t][s][f-1])

print(dp[-1][-1][-1])