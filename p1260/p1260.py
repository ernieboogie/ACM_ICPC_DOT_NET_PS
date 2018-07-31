import sys

def edge_exist(edge_list, vertex):
    for edge in edge_list:
        if vertex in edge:
            return True
    return False:

_init = list(map(int, sys.stdin.readline().rstrip().split(" ")))

vertex = list(range(1, _init[0] +  1))
num_edge = _init[1]
start = _init[2]

edge = []
for _ in range(num_edge):
    new_edge = []
    edge_info = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    new_edge.append(edge_info[0])
    new_edge.append(edge_info[1])
    edge.append(new_edge)


#DFS
dfs_edge = edge
dfs_vertex = vertex
dfs_answer = ''

current_vertex = start
while len(dfs_vertex):
    dfs_vertex.remove(current_vertex)



#BFS
bfs_edge = edge
bfs_vertex = vertex
bfs_answer = ''
current_vertex = start

while len(bfs_vertex):
    bfs_vertex.remove(current_vertex):

    while :
