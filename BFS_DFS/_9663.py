n = int(input())

result = 0
row = [0] * n

def isMovable(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def Nqueen(x):
    global result
    if x == n:
        result += 1
        return

    else:
        for i in range(n):
            row[x] = i
            if isMovable(x):
                Nqueen(x+1)

Nqueen(0)
print(result)