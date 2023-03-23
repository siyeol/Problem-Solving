N = int(input())

conf = list()
for _ in range(N): 
    conf.append(list(map(int, input().split())))

conf.sort(key = lambda x :x[0])
conf.sort(key = lambda x :x[1])

cur = 0
count = 0
for conference in conf:
    if conference[0] >= cur:
        cur = conference[1]
        count += 1

print(count)