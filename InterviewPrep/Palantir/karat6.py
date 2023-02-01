all_courses = [
    ["Logic", "COBOL"],
    ["Data Structures", "Algorithms"],
    ["Creative Writing", "Data Structures"],
    ["Algorithms", "COBOL"],
    ["Intro to Computer Science", "Data Structures"],
    ["Logic", "Compilers"],
    ["Data Structures", "Logic"],
    ["Creative Writing", "System Administration"],
    ["Databases", "System Administration"],
    ["Creative Writing", "Databases"],
    ["Intro to Computer Science", "Graphics"],
]

#DFS
#adj list

graph = dict()
ends = list()

for start, end in all_courses:
    ends.append(end)
    if start not in graph:
        graph[start] = [end]
    else:
        graph[start].append(end)

#find root
roots = []
for key in graph.keys():
    if key not in ends:
        roots.append(key)

answer = list()

def DFS(root, search):
    if root not in graph.keys():
        temp_list = list(search.split(sep=", "))
        answer.append(temp_list[(len(temp_list)-1)//2])
        return
    for next in graph[root]:
        visited[next] = 1
        DFS(next, search+", "+str(next))
        visited[next] = 0


for root in roots:
    visited = dict()
    for key in graph.keys():
        visited[key] = 0
    search = root
    DFS(root, root)

print(list(set(answer)))



