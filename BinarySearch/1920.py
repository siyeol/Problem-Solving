# # https://www.acmicpc.net/step/29
# https://yu5501.tistory.com/80

# # arr = [4, 1, 5, 2, 3]
# # N = 5


def binary_search(N, arr):

    left = 0
    right = len(arr)-1
    
    while left<=right:
    
        mid = (left+right)//2
    
        if arr[mid] == N:
            return mid

        elif arr[mid]>N:
            right = mid-1

        else:
            left = mid+1

    return -1

N = int(input())

Narr = list(map(int, input().split()))


M = int(input())

Marr = list(map(int, input().split()))


Narr.sort()


for elem in Marr:
    if binary_search(elem, Narr) == -1:
        print("0")
    else:
        print("1")
    
