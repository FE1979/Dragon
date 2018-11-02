import random

#transform graph notated in roots into dictionary
def make_graph_dict(roots):
    graph = {}
    for i in roots:
        if i[0] not in graph:
            graph[i[0]] = []
        graph[i[0]].append(i[1])
    return graph

#extracts nodes from roots
def collect_nodes(roots):
    nodes = []

    for i in roots:
        for j in i:
            if j not in nodes:
                nodes.append(j)
    nodes.sort()

    return nodes

#transform graph notated in roots into matrix (numbers only)
def make_graph_matrix(roots):

    nodes = collect_nodes(roots)
    n = len(nodes)
    matrix = [[0 for i in range(n+1)] for i in range(n+1)]


    for i in roots:
        matrix[i[0]][i[1]] = 1

    return matrix

#explores graph notated as dictionary
def BFS_dict(graph, start):
    explored = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        print('\n', node, queue)
        if node not in explored:
            explored.append(node)
            neighbours = graph.get(node)
            if neighbours is not None:
                for i in neighbours:
                    queue.append(i)
        pass
    return explored

#search shortest path or all paths if no end
def BFS_dict_path(graph, start, end = None):
    explored = [] #nodes visited
    queue = [[start]] #init script with starting point
    paths = [] #return all paths if no end
    if start == end: #obviuos solution
        return end

    while queue: #do script until queue exists
        path = queue.pop(0) #take first path in queue
        node = path[-1] #check an end of this path
        if node not in explored: #if the end of the path is not explored
            neighbours = graph.get(node) #take all neighbours to the end of path
            if neighbours is not None: #if there are neighbours from the node
                for i in neighbours: #create new paths and add them to queue
                    new_path = path[:]
                    new_path.append(i)
                    queue.append(new_path)
                    if i == end: #if we reach the end return path, if end == None the path will never returned
                        return new_path
            else:
                paths.append(path) #if there are no neighbours just place the path into paths collection
            explored.append(node) #mark the node as explored

    return paths #return all paths if no end as argument

def BFS_root_path(root, start, end = None):
    explored = []
    queue = [[start]]
    paths = []

    if start == end:
        return end

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = []
            for i in roots:
                if i[0] == node:
                    neighbours.append(i[1])
            if neighbours != []:
                for i in neighbours:
                    new_path = path[:]
                    new_path.append(i)
                    queue.append(new_path)
                    if i == end:
                        return new_path
            else:
                paths.append(path)
            explored.append(node)

    return paths

def BFS_matrix_path(matrix, start, end = None):
    explored = []
    queue = [[start]]
    paths = []

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = []
            i = 0
            while i < len(matrix[node]):
                if matrix[node][i] != 0:
                    neighbours.append(i)
                i += 1

            if neighbours != []:
                for i in neighbours:
                    new_path = path[:]
                    new_path.append(i)
                    queue.append(new_path)
                    if i == end:
                        return new_path
            else:
                paths.append(path)
            explored.append(node)

    return paths

#example of graph
roots = [[1, 2], [1, 3], [2, 4],[2, 1], [2, 5], [3, 6], [6, 7], [4, 8], [5, 9], [5, 10], [10, 11]]

choice = int(input("""Choose a type of graph notation
1 for Dictionary, 2 for matrix, 3 - simple roots'\n>"""))
start = int(input('Type node to start >'))
try:
    end = int(input('Type end node or type Enter to search all paths >'))
except ValueError:
    end = None

if choice == 1:
    graph_1 = make_graph_dict(roots)
    path = BFS_dict_path(graph_1, start, end)
    print('\nThe graph is:\n{}\n'.format(graph_1))
    print('Path from {} to {} is:\n {}'.format(start,end,path))
elif choice == 2:
    graph_1 = make_graph_matrix(roots)
    path = BFS_matrix_path(graph_1, start, end)
    print('\nThe graph is:\n{}\n'.format(graph_1))
    print('Path from {} to {} is:\n {}'.format(start,end,path))
elif choice == 3:
    path = BFS_root_path(roots, start, end)
    print('\nThe graph is:\n{}\n'.format(roots))
    print('Path from {} to {} is:\n {}'.format(start,end,path))
else:
    print("""I don't understand you. Bye!""")
