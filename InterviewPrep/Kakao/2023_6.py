import sys
sys.setrecursionlimit(5000)

direction = dict()
direction['d'] = [1, 0]
direction['l'] = [0, -1]
direction['r'] = [0, 1]
direction['u'] = [-1, 0]

def solution(n, m, x, y, r, c, k):
    board = [[0]*m for _ in range(n)]
    starty, startx = x-1, y-1
    endy, endx = r-1, c-1
    
    result_list = list()
    
    def manhat_dist(y1, x1, y2, x2):
        return abs(y1-y2)+abs(x2-x1)
    
    def DFS(y, x, route):
        if y==endy and x==endx and len(route)==k:
            result_list.append(route)
            return
        for key, (dy, dx) in direction.items():
            yy = y+dy
            xx = x+dx
            if 0<=yy<n and 0<=xx<m and manhat_dist(yy,xx,endy,endx) <= (k-len(route)):# 
                DFS(yy, xx, route+key)
                break
                
    DFS(starty, startx, '')
    
    if result_list:
        result_list.sort()
        return result_list[0]
    else:
        return "impossible"