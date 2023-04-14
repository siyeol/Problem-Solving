K, N = map(int, input().split())
arr = list()

for _ in range(K):
    arr.append(int(input()))

left = 1
right = 1000000

while left <= right:
    mid = (left+right)//2

    temp = 0
    for lan in arr:
        temp += (lan//mid)
    
    if temp < N:
        right = mid-1
    else:
        left = mid+1

print(right)