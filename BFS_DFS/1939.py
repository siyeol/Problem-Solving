from collections import deque

N, M = map(int, input().split())

island = [[] for _ in range(N)]

for _ in range(M):
    start, end, weight = map(int, input().split())
    island[start-1].append((end-1, weight))
    island[end-1].append((start-1, weight))

FacA, FacB = map(int, input().split())
FacA -= 1
FacB -= 1

def BFS(X):
    visited = [0] * N

    q = deque()
    q.append(FacA)
    visited[FacA] = 1
    
    while q:
        nextq = q.popleft()
        if nextq == FacB:
            return True
        for dest,weight in island[nextq]:
            if not visited[dest] and weight >= X:
                visited[dest]=1
                q.append(dest)
    
    return False

right = 1000000000
left = 1

while left<=right:
    mid = (left+right)//2
    if BFS(mid):
        left = mid+1
    else:
        right = mid-1

print(right)