from collections import Counter

N = int(input())

arr = list(map(int, input().split()))
cnt_dict = Counter(arr)

arr_nodup = list(set(arr))
arr_nodup.sort()

M = int(input())
query = list(map(int, input().split()))

def binary_search(arr, X):
    left = 0
    right = len(arr)-1

    while left<=right:
        mid = (left+right)//2

        if arr[mid] == X:
            return mid
        elif arr[mid]>X:
            right = mid-1
        else:
            left = mid+1

    return -1


answer = list()
for q in query:
    idx = (binary_search(arr_nodup, q))
    if idx != -1:
        cnt = cnt_dict[arr_nodup[idx]]
        answer.append(cnt)
    else:
        answer.append(0)

for ans in answer:
    print(ans, end=" ")