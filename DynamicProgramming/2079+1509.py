palin = list(input())
L = len(palin)

dp_palin = [[0]*L for _ in range(L)]

#itself
for i in range(L):
    dp_palin[i][i]=1

#adjacent
for i in range(L-1):
    if palin[i]==palin[i+1]:
        dp_palin[i][i+1] = 1

#etc
for l in range(3, L + 1):
    for start in range(L - l + 1):
        end = start + l - 1
        if palin[start] == palin[end] and dp_palin[start + 1][end - 1]:
            dp_palin[start][end] = 1

dp_substr = [3000 for _ in range(L+1)]
dp_substr[0]=0

#realDP
for i in range(L):
    dp_substr[i+1] = min(dp_substr[i+1], dp_substr[i] + 1)
    for j in range(i, L):
        if dp_palin[i][j]!=0:
            dp_substr[j+1] = min(dp_substr[j+1], dp_substr[i] + 1)
            # print(dp_substr)

print(dp_substr[-1])


# REFERENCE: https://velog.io/@sunkyuj/python-백준