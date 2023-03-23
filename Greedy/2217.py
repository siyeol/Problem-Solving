N = int(input())

rope_list = list()
for _ in range(N): 
    rope_list.append(int(input()))

rope_list.sort()
max_total = 0
for idx in range(N):
    max_total = max(max_total, rope_list[idx]*(N-idx))

print(max_total)
