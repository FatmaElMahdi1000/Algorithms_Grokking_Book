print("*******Right way for graph creation _ modeling the connections***********")
def add_edge(graph, node, neighbours):
    if node not in graph:
        graph[node] = []  #ensuring main node exist
    for neighbour in neighbours:
        if neighbour not in graph: 
            graph[neighbour] = [] #add each neighbour as a node(key) as well, even if it's going to have no out neighbours
        graph[node].append(neighbour)
    return graph

graph = {} #dict/hash table
print(add_edge(graph, 'You', ['mother','father']))
print(add_edge(graph, 'mother', ['sisters','brothers']))

print("*******another way for graph creation***********")
"""So simple without considering every outneighbour is a node as well"""
graph2 = {}
graph2["you"]  = ['mother', 'father']
graph2['mother'] = ['sisters', 'brother']
print(graph2)