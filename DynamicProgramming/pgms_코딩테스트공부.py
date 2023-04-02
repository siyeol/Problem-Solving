from math import inf

def solution(alp, cop, problems):
    
    max_alp, max_cop = 0, 0
    
    for problem in problems:
        max_alp = max(max_alp, problem[0])
        max_cop = max(max_cop, problem[1])
    
    dp = [[inf]*(max_alp+1) for _ in range(max_cop+1)]
    
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)

    dp[cop][alp] = 0
    
    for y in range(cop, max_cop+1):
        for x in range(alp, max_alp+1):
            if y < max_cop:
                dp[y+1][x] = min(dp[y][x]+1, dp[y+1][x])
            if x < max_alp:
                dp[y][x+1] = min(dp[y][x]+1, dp[y][x+1])
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if x >= alp_req and y>=cop_req:
                    next_alp = min(max_alp, x+alp_rwd)
                    next_cop = min(max_cop, y+cop_rwd)
                    dp[next_cop][next_alp] = min(dp[next_cop][next_alp], dp[y][x]+cost)
            
    return dp[max_alp][max_cop]


print(solution(10,	10	,[[10,15,2,1,2],[20,20,3,3,4]]))
print(solution(0,	0,	[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]	))