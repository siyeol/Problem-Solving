import math

N = int(input())

arr = list(map(int, input().split()))

master, sub = map(int, input().split())

cnt = 0

for test in arr:
    if test <= master:
        cnt+=1
        continue
    test -= master
    cnt+=1
    cnt+= math.ceil(test/sub)    

print(cnt)
