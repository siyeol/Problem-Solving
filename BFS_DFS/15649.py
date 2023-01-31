#Permutation

N, M = map(int, input().split())

arr = [i for i in range(1, N+1)]


result = list()

def DFS(start, string, cnt):
    if cnt == M:
        print(string)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            temp = string + str(arr[i]) + " "
            DFS(i, temp, cnt+1)
            visited[i] = 0

for idx, elem in enumerate(arr):
    visited = [0] * (N)
    visited[idx] = 1
    DFS(idx, str(elem) + " ", 1)

'''
Combination
N, M = map(int, input().split())

arr = [i for i in range(1, N+1)]


result = list()


def DFS(start, string, cnt):
    if cnt == M:
        print(string)
        return

    for i in range(start, N):
        if not visited[i]:
            visited[i] = 1
            temp = string + str(arr[i]) + " "
            DFS(i, temp, cnt+1)

for idx, elem in enumerate(arr):
    visited = [0] * (N)

    DFS(idx, "",0)
'''
