from collections import deque

example = [
[0,1,1,1,1,1],
[0,1,0,0,0,1],
[0,1,0,0,0,1],
[0,1,1,1,1,1],
[0,0,0,0,0,0],
[0,0,1,1,1,0],
[0,0,1,0,1,0],
[0,0,1,1,1,0],
]

dy = [0, 1, -1, 0]
dx = [1, 0, 0, -1]

def find_corner(board):
    Y = len(board)
    X = len(board[0])

    visited = [[0]*X for _ in range(Y)]

    def BFS(y, x):
        q = deque()
        q.append((y, x))
        visited[y][x]=1

        max_x = x
        max_y = y

        while q:
            cur_y, cur_x = q.popleft()

            for i in range(2):
                new_y = cur_y + dy[i]
                new_x = cur_x + dx[i]

                if 0<=new_y<Y and 0<=new_x<X:
                    if not visited[new_y][new_x] and board[new_y][new_x] == 1:
                        q.append((new_y, new_x))
                        visited[new_y][new_x] = 1

                        max_x = max(max_x, new_x)
                        max_y = max(max_y, new_y)

        width =  max_x - x +1
        height = max_y - y +1

        return width, height

    result = list()
    for y in range(Y):
        for x in range(X):
            if board[y][x] == 1 and not visited[y][x]:
                w, h = BFS(y, x)
                result.append([x, y, h, w])

    return result
print(find_corner(example))