h, w = map(int, input().split())
heights = list(map(int, input().split()))

answer = [0]*h

for i in range(h):
    t = -1
    for j in range(w):
        if heights[j] > i:
            if t == -1:
                t = 0
            else:
                answer[i] += t
                t = 0
        else:
            if t != -1:
                t += 1

print(sum(answer))
