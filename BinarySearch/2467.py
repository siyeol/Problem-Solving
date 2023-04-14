from math import inf

N = int(input())
arr = list(map(int, input().split()))

arr.sort()

left = 0
right = len(arr)-1

min_val = inf
minl, minr = None, None

while left<right:
    temp_sum = arr[left]+arr[right]

    if min_val >= abs(temp_sum):
        min_val = abs(temp_sum)
        minl, minr = left, right

    if temp_sum > 0:
        right -= 1
    elif temp_sum < 0:
        left += 1
    else:
        break

print(arr[minl], arr[minr])

