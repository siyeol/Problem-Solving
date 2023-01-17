from collections import deque
from dis import dis
N, M = map(int, input().split())

graph = [[]for _ in range(N+1)]
for _ in range(N-1):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))

se_list = list()
for _ in range(M):
    start, end = map(int, input().split())
    se_list.append((start, end))
# start, end = map(int, input().split())

#BFS
for start, end in se_list:
    q = deque()
    q.append((start, 0))
    visited = [False]*(N+1)
    visited[start] = True
    def BFS():
        while q:
            cur, dist = q.popleft()
            if cur == end:
                return dist
            for new, new_dist in graph[cur]:
                if not visited[new]:
                    q.append((new, dist+new_dist))
                    visited[new]=True
                    
    print(BFS())