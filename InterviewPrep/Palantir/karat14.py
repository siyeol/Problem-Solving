
board3 = [
    [  1,  0,  0, 0, 0 ],
    [  0, -1, -1, 0, 0 ],
    [  0, -1,  0, 1, 0 ],
    [ -1,  0,  0, 0, 0 ],
    [  0,  1, -1, 0, 0 ],
    [  0,  0,  0, 0, 0 ],
]

start = (0, 0)
end = (4, 1)

from collections import deque

Y = len(board3)
X = len(board3[0])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_all_treasure(board, start, end):
    #save location of treasure
    treasure_list = list()
    for y in range(Y):
        for x in range(X):
            if board[y][x] == 1:
                treasure_list.append((y, x))
    # print(treasure_list)
    
    #find shortest path from start to end/save route
    
    visited = [[0] * X for _ in range(Y)]

    track_list = list()
    track = ""
    def DFS(y, x, track):
        
        if y == end[0] and x == end[1]:
            track_list.append(track)
        
        for i in range(4):
            newy = y+dy[i]
            newx = x+dx[i]
            
            if 0<=newy<Y and 0<=newx<X:
                if not visited[newy][newx] and board[newy][newx]!=-1:
                    visited[newy][newx] = 1
                    pos = "(%d, %d), "%(newy, newx)
                    DFS(newy, newx, track+pos)
                    visited[newy][newx] = 0
           
    visited[start[0]][start[1]] = 1
    pos = "(%d, %d), "%(start[0], start[1])
    track += pos
    DFS(start[0], start[1], track)
    
    find_min = list()
    for track in track_list:
        flag = False
        for treasure in treasure_list:
            # print(str(treasure))
            if str(treasure) not in track:
                flag = True
        
        if flag is False:
            find_min.append(track)
            
    if len(find_min) ==0:
        return None
         
    find_min.sort(key = lambda x: len(x.split(sep="), (")))
            
    return (find_min[0])
    # print(len(find_min))
    

print(find_all_treasure(board3, start, end))
start = (5, 0)
end = (0, 4)
print(find_all_treasure(board3, start, end))



def can_everywhere(board, start):
    #count whole zeros
    count_zero=0
    
    
    addup = 0
    for row in board:
        addup += sum(row)
    
    count_zero = X*Y + addup
       
    
    #BFS to mark all visited
    
    #LRDU
    
    visited = [[0] * X for _ in range(Y)]

    def BFS(y, x):
        
        q = deque()
        q.append((y, x))
        visited[y][x] = 1
        
        while q:
            cury, curx = q.popleft()
            
            for i in range(4):
                newy = cury+dy[i]
                newx = curx+dx[i]
                
                if 0<=newy<Y and 0<=newx<X:
                    if not visited[newy][newx] and board[newy][newx]!=-1:
                        q.append((newy, newx))
                        visited[newy][newx] = 1
                        
    BFS(start[0], start[1])
    
    count_visited = 0
    for row in visited:
        count_visited += sum(row)           
            
    #add all visited(1) and compare with num of zeros
    if count_visited == count_zero:
        return True
    else:
        return False

# print(can_everywhere(board3, start))