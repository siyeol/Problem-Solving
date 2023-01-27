from collections import deque

N, K = map(int, input().split())

def BFS(n):
    q = deque()
    q.append(n)
    while q:
        new_n = q.popleft()
        if new_n == K:
            return visited[new_n]
        
        for next_n in (new_n+1, new_n-1, new_n*2):
            if 0<=next_n<MAX_LINE and not visited[next_n]:
                q.append(next_n)
                visited[next_n] = visited[new_n]+1


MAX_LINE = 100001
visited = [0] * MAX_LINE

print(BFS(N))