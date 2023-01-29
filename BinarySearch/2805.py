N, M = map(int, input().split())

arr = list(map(int, input().split()))

left = 1
right = max(arr)

while left<=right:
    mid = (left+right)//2

    temp_sum = 0
    for tree in arr:
        if tree > mid:
            temp_sum+=(tree - mid)

    if temp_sum >= M:
        left = mid+1
    else:
        right = mid-1

print(right)