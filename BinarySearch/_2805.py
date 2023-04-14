N, M = map(int, input().split())
arr = list(map(int, input().split()))

left = 1
right = max(arr)

while left <=right:
    mid = (left+right)//2

    temp = 0
    for tree in arr:
        if tree >= mid:
            temp+=(tree-mid)
    
    if temp >= M:
        left = mid+1
    else:
        right = mid-1

print(right)