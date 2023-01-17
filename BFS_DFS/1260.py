from collections import deque

N, M, V = map(int, input().split())

graph = [[0]*(N+1) for _ in range(N+1)]
visited_BFS = [False]* (N+1)
visited_DFS = [False]* (N+1)

for _ in range(M):
    s, e = map(int, input().split())
    graph[s][e] = 1
    graph[e][s] = 1

def BFS():
    q = deque()
    q.append(V)
    visited_BFS[V]=True

    while q:
        v_cur = q.popleft()
        print(v_cur, end=" ")
        for i in range(1, N+1):
            if graph[v_cur][i] and not visited_BFS[i]:
                q.append(i)
                visited_BFS[i]=True

def DFS(v_cur):
    visited_DFS[v_cur] = True
    print(v_cur, end=" ")
    for i in range(1, N+1):
        if graph[v_cur][i] and not visited_DFS[i]:
            DFS(i)



DFS(V)
print()

BFS()
