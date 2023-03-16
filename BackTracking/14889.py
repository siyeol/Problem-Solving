from math import inf
N = int(input())

arr = list()
for _ in range(N):
    arr.append(list(map(int, input().split())))

people = [i for i in range(N)]
visited = [0]*N

max_result = inf

def DFS(idx, team_len):
    if team_len == N/2:
        global max_result
        A = 0
        B = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    A += arr[i][j]
                elif not visited[i] and not visited[j]:
                    B += arr[i][j]
        max_result = min(max_result, abs(A-B))
        return
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = 1
            DFS(i+1, team_len+1)
            visited[i] = 0

DFS(0, 0)
print(max_result)
