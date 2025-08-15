from collections import deque

def add_edge(graph, node, neighbours):  
    """
    Building the directed graph ("in neighbours, out neighbours")
    Args:
        graph: hashtable/dict
        node: starting node
        neighbours: out neighbours
    Return:
        graph/ dicitionary/ hashtable
    """
    if node not in graph:
        graph[node] = []  #ensuring main node exist
    for neighbour in neighbours:
        if neighbour not in graph: 
            graph[neighbour] = [] #add each neighbour as a node(key) as well, even if it's going to have no out neighbours
        graph[node].append(neighbour)
    return graph

def person_is_seller(name):
    """
    takes the person name check if it ends with m 
    Args:
        name (could be graph neighber's)
    Return:
        True or False
    """
    return name[-1] == 'm' 

def BFS(name):
    """
    breadth First search method
    Args:
        name:  (could be graph neighber's)
    Return:
        List: list of mango sellers in this network
    """
    """Building the queue"""
    searched = [] #an array to keep track of which people you searched before
    search_queue= deque() #creates a new queue
    search_queue += graph['you']   # start with neighbors of the starting node
    
    while search_queue: #while the queue isn't empty
        person = search_queue.popleft() #method to pop/rm from the left (Queue follows FIFO principle)
        if not person in searched: #only search the person if you've not already searched 
            if person_is_seller(person): #if True
                print(person, " is a mango seller!")
                return True
            else:
                search_queue += graph[person] #we popped off the person, we checked and he's/she's not a mango seller, now adding the outneighbours to the queue to check if there's a mango seller again among them (returning to while loop) -->this is checking the following degree connection
                searched.append(person)
    return False #no seller found in the entire network

graph = {} #dict/hash table
add_edge(graph, 'you', ['mother','father']) #You is the starting node
add_edge(graph, 'mother', ['sisters','brothers'])
add_edge(graph, 'father', ['tom', 'sam'])  # someone ending in 'm'
BFS('you') #Running BFS

"""Note: the reason it found "tom" instead of "sam", when both names end with 'm', is because BFS always finds the closest match first. not only the match
but also the closest one"""










