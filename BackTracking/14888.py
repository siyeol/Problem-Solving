from math import inf
N = int(input())
arr = list(map(int, input().split()))

# + - x /
arith = list(map(int, input().split()))

min_result = inf
max_result = -inf

def backtrack(result, idx):
    if idx == len(arr):
        global min_result, max_result
        min_result = min(min_result, result)
        max_result = max(max_result, result)
        return

    if arith[0] > 0:
        arith[0]-=1
        backtrack(result+arr[idx], idx+1)
        arith[0]+=1
    if arith[1] > 0:
        arith[1]-=1
        backtrack(result-arr[idx], idx+1)
        arith[1]+=1
    if arith[2] > 0:
        arith[2]-=1
        backtrack(result*arr[idx], idx+1)
        arith[2]+=1
    if arith[3] > 0:
        arith[3]-=1
        if result >= 0:
            backtrack(result//arr[idx], idx+1)
        else:
            backtrack(-(-result//arr[idx]), idx+1)
        arith[3]+=1

backtrack(arr[0], 1)

print(max_result)
print(min_result)