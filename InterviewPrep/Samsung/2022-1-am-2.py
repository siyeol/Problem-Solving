n, m, h, k = map(int, input().split())

lry = [0, 0]
lrx = [1, -1]

udy = [1, -1]
udx = [0, 0]

runners = list()
for _ in range(m):
    y, x, d = map(int, input().split())
    if d == 1:
        runners.append([y-1, x-1, "lr", 0])
    elif d == 2:
        runners.append([y-1, x-1, "ud", 0])

trees = set()
for _ in range(h):
    y, x = map(int, input().split())
    trees.add((y-1, x-1))

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

midy, midx = n//2, n//2

route = [] # y, x, dir
dir_route = []
route.append((midy, midx))

# visited = [[0] * width for _ in range(width)]
visited = [[0] * n for _ in range(n)]
visited[midy][midx] = 1

cury, curx = n//2, n//2

for i in range(1, n//2+1):
    width = i*2 + 1

    while True:
        if len(route) == width**2:
            break
        for di in range(4):
            yy = cury + dy[di]
            xx = curx + dx[di]

            if midy-i<=yy<=midy+i and midx-i<=xx<=midx+i and not visited[yy][xx]:
                visited[yy][xx] = 1
                route.append((yy,xx))
                dir_route.append(di)
                cury = yy
                curx = xx
                break

dir_route.append(0)

def should_move(y1, x1, y2, x2):
    if abs(y1-y2)+abs(x1-x2)<=3:
        return True
    else:
        return False

sooly = n//2
soolx = n//2
soold = 0
soolidx = 0
idx_dir = 1
isFirst = False

dir_route_oppo = list()

for dr in dir_route:
    dir_route_oppo.append((dr+2)%4)

def move_sooleh():
    global soolx, sooly, soold, soolidx, idx_dir

    if soolidx == 0:
        idx_dir = 1
    elif soolidx == len(route)-1:
        idx_dir = -1

    soolidx += idx_dir
    sooly, soolx = route[soolidx]

    if idx_dir == 1:
        soold = dir_route[soolidx]
    elif idx_dir == -1:
        soold = dir_route_oppo[soolidx]

    
    isFirst = True
    print(sooly, soolx, soold)

for i in range(27):
    move_sooleh()

print(runners)
print(trees)
print(route)
print(dir_route)

print(len(route), len(dir_route))