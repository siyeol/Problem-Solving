# from itertools import permutations
N, S = map(int, input().split())

total = list(map(int, input().split()))

cumul_sum = [0]*(N)

cumul_sum[0]= total[0]
for i in range(1, N):
    cumul_sum[i]=cumul_sum[i-1]+total[i]

cumul_sum.insert(0, 0)



def consec():
    answer = 1000001
    start = 0
    end = 1
    while start != N:
        if cumul_sum[end]-cumul_sum[start]>=S:
            if end - start < answer:
                answer = end - start
            start += 1
        else:
            if end != N:
                end +=1
            else:
                start +=1
              
    if answer!= 1000001:
        return answer
    else:
        return 0

print(consec())