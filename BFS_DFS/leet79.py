class Solution:
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        Y = len(board)
        X = len(board[0])

        def DFS(word_idx, visited, y, x):
            if word_idx == len(word):
                return True

            for i in range(4):
                yy = y+dy[i]
                xx = x+dx[i]

                if 0<=yy<Y and 0<=xx<X:
                    if not visited[yy][xx] and word[word_idx] == board[yy][xx]:
                        visited[yy][xx]=1
                        if DFS(word_idx+1, visited, yy, xx):
                            return True
                        visited[yy][xx]=0

            return False

        for y in range(Y):
            for x in range(X):
                if word[0] == board[y][x]:
                    visited = [[0]*X for _ in range(Y)]
                    visited[y][x]=1
                    if DFS(1, visited, y, x):
                        return True

        return False