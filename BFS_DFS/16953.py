from collections import deque

A, B = map(int, input().split())

cnt = 0

q = deque()
q.append((A, cnt))

def BFS(q):
    while q:
        a, cnt = q.popleft()
        if a == B:
            return cnt
        elif a>B:
            continue
        else:
            q.append((2*a, cnt+1))
            q.append((int(str(a)+"1"), cnt+1))

out = BFS(q)   
if out is None:
    print(-1)
else:
    print(out+1)