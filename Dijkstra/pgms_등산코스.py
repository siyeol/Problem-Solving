import heapq
from math import inf

def solution(n, paths, gates, summits):
    graph = dict()
    for path in paths:
        if path[0] not in graph:
            graph[path[0]] = [(path[1], path[2])]
        else:
            graph[path[0]].append((path[1], path[2]))    

        if path[1] not in graph:
            graph[path[1]] = [(path[0], path[2])]
        else:
            graph[path[1]].append((path[0], path[2]))    
    
    summits.sort()
    set_summits = set(summits)

    visited = [inf] * (n+1)
    hq = []

    for gate in gates:
        heapq.heappush(hq, (0, gate))
        visited[gate] = 0
    
    while hq:
        intense, start = heapq.heappop(hq)

        if start in set_summits:
            continue

        if intense > visited[start]:
            continue

        for dest, weight in graph[start]:
            intense_update = max(intense, weight)
            if intense_update < visited[dest]:
                visited[dest] = intense_update
                heapq.heappush(hq, (intense_update, dest))

    answer = [0, inf]
    for smt in summits:
        if answer[1] > visited[smt]:
            answer[0] = smt
            answer[1] = visited[smt]
    
    return answer
    
print(solution(6,[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],	[1, 3],	[5]))
