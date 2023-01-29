K, N = map(int, input().split())

cable = [0]*K
for k in range(K):
    cable[k] = int(input())

cable.sort()

def binary_search(arr, N):
    left = 1
    right = arr[-1]

    while left<=right:
        mid = (left+right)//2

        cnt = 0
        for elem in arr:
            cnt += elem//mid
        
        if cnt >= N:
            left = mid+1
        else:
            right = mid-1

    return right

print(binary_search(cable, N))
