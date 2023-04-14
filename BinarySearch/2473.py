from math import inf

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

mid = len(arr)//2

min_val = inf

min1, min2 = None, None
min0 = None

for i in range(N-2):
    left_idx = i+1
    right_idx = len(arr)-1
    midpoint = arr[i] #BEWARE!

    while left_idx<right_idx:
        temp = (midpoint + arr[left_idx] + arr[right_idx])
        
        if abs(temp) <= abs(min_val):
            min_val=temp
            min1, min2 = left_idx, right_idx
            min0 = midpoint

        if temp > 0 :
            right_idx-=1
        
        elif temp < 0:
            left_idx+=1

        else:
            print(min0, arr[min1], arr[min2])
            exit()



print(min0, arr[min1], arr[min2])

