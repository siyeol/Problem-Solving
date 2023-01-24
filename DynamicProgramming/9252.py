first = input()
second = input()

flen = len(first)+1
slen = len(second)+1
str_dp = [[""]*(flen) for _ in range(slen)]


for f in range(1, flen):
    for s in range(1, slen):
        if first[f-1] == second[s-1]:
            str_dp[s][f] = str_dp[s-1][f-1]+first[f-1]
        else:
            if len(str_dp[s-1][f]) > len(str_dp[s][f-1]): #max 대신
                str_dp[s][f] = str_dp[s-1][f]
            else:
                str_dp[s][f] = str_dp[s][f-1]

print(len(str_dp[-1][-1]))
if len(str_dp[-1][-1]):
    print(str_dp[-1][-1])