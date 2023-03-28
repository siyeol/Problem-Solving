from math import inf
S = (input())

M = int(input())

erase = {}
for _ in range(M):
    key, val = input().split()
    erase[key] = int(val)

dp = [-inf] * (len(S))

def checker(start):
    global dp

    if start>=len(S):
        return 0
    if dp[start] != -inf:
        return dp[start]
    
    dp[start] = checker(start+1)+1

    for key in erase:
        if S[start:start+len(key)] == key:
            dp[start] = max(dp[start], checker(start+len(key))+erase[key])

    return dp[start]

print(checker(0))

#Reference: https://velog.io/@primrose_/Python-BOJ-%EB%B0%B1%EC%A4%80-21941-%EB%AC%B8%EC%9E%90%EC%97%B4%EC%A0%9C%EA%B1%B0
