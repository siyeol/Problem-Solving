n = int(input())

fibo = [0] * 100

fibo[0]=0
fibo[1]=1

for i in range(n):
    fibo[i+2] = fibo[i]+fibo[i+1]

print(fibo[n])