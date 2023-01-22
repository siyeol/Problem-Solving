a, b = map(int, input().split())
c, d = map(int, input().split())
x, y = map(int, input().split())

def CCW (a, b, c, d, x, y):
    return (c-a)*(y-b) - (x-a)*(d-b)

ccw = CCW(a, b, c, d, x, y)

if ccw==0:
    print(0)
elif ccw>0:
    print(1)
else:
    print(-1)