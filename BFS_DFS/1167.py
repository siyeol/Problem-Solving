import sys 
sys.setrecursionlimit(10**6)

n = int(input())

tree = [[] for _ in range(n)]

for _ in range(n):
    input_list = list(map(int, input().split()))
    start = input_list.pop(0)

    for idx in range(len(input_list)-1):
        if idx%2 == 0:
            end = input_list[idx]
            weight = input_list[idx+1]
            tree[start-1].append([end-1, weight])
            
            
dist1_list = [-1] * n
dist2_list = [-1] * n

def DFS(node, dist, dist_list):
    for end, weight in tree[node]:
        if dist_list[end] == -1:
            dist_list[end] = dist + weight
            DFS(end, dist+weight, dist_list)

dist1_list[0] = 0
DFS(0, 0, dist1_list)

max_idx = dist1_list.index(max(dist1_list))
dist2_list[max_idx] = 0
DFS(max_idx, 0, dist2_list)

print(max(dist2_list))
