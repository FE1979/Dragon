"""
Deep first search script
"""
#transform graph notated in roots into dictionary
def make_graph_dict(roots):
    graph = {}
    for i in roots:
        if i[0] not in graph:
            graph[i[0]] = []
        graph[i[0]].append(i[1])
    return graph

#explores DFS graph notated as dictionary
def DFS_dict(graph, start):
    explored = []
    queue = [start]

    while queue:
        node = queue.pop()
        if node not in explored:
            explored.append(node)
            neighbours = graph.get(node)
            if neighbours is not None:
                for i in neighbours:
                    queue.append(i)
        pass
    return explored

#search shortest path or all paths if no end
def DFS_dict_path(graph, start, end = None):
    explored = [] #nodes visited
    queue = [[start]] #init script with starting point
    paths = [] #return all paths if no end
    if start == end: #obviuos solution
        return end

    while queue: #do script until queue exists
        path = queue.pop() #take first path in queue
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

#example of graph
roots = [[1, 2], [1, 3], [2, 4],[2, 1], [2, 5], [3, 6], [6, 7], [4, 8], [5, 9], [5, 10], [10, 11]]

GRAPH = make_graph_dict(roots)

print('Let take this graph:\n', GRAPH,'\n')
print('and travel to each node:\n', DFS_dict(GRAPH, 1))
print('\n')
print('A paths are:\n', DFS_dict_path(GRAPH, 1))
