tree = [[1,4], [1,5], [2,5], [3,6], [6, 7], [5, 9], [4, 11]]

def findParent(tree):
    edge = dict()
    
    for start, end in tree:
        if end not in edge:
            edge[end] = [start]
        else:
            edge[end].append(start)
            
    zeroP = list()
    oneP = list()
    for key, value in edge.items():
        if len(value)==0:
            zeroP.append(key)
        elif len(value) == 1:
            oneP.append(key)
    return zeroP, oneP
    # print(edge)
    
# print(findParent(tree))

from collections import deque

def hasCommonAncestor(tree, X, Y):
    edge = dict()
    
    for start, end in tree:
        if end not in edge:
            edge[end] = [start]
        else:
            edge[end].append(start)
        
    Xances = list()
    Yances = list()
    
    
    # visited = {x:0 for x in edge.keys()}
    # print(visited)
    # return
    def BFS(X, Xances):
        # visited = {x:0 for x in edge.keys()}
        q = deque()
        q.append(X)
        # visited[X] = 1
        Xances.append(X)
        while q:
            cur = q.popleft()
            if cur not in edge:
                continue
            for parent in edge[cur]:
                if parent not in Xances:
                    Xances.append(parent)
                    q.append(parent)
                        
    BFS(X, Xances)
    BFS(Y, Yances)
    Xances.pop(0)
    Yances.pop(0)
    
    
    for xa in Xances[::-1]:
        for ya in Yances[::-1]:
            if xa == ya:
                return xa
    return None
            
        
print(hasCommonAncestor(tree, 11, 9))