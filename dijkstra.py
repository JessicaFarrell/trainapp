import string
import random

## a set of functions that perform dijkstras shortest path

def dijkstra(route = ['A', 'B'], graph={}, nodes=[]):

    unvisited = {}
    visited = {}
    current = route[0]
    currentDistance = 0
    # variable to keep track of the path taken
    previous = {}
    for node in nodes:
        unvisited[node] = None
        previous[node] = None
    unvisited[current] = currentDistance
    while True:
        
# =============================================================================
#         GO OVER ALL THE NEIGHBOURS AND FIND THEIR DISTANCES
#         KEEP TRACK OF THE MINIMUM DISTANCE FOR EACH NEIGHBOUR
# =============================================================================
        
        # get the connected places and their distance from the current place.
        if current in graph:
            for neighbour, distance in graph[current].items():
                # if we've visited the node, skip it
                if neighbour not in unvisited: continue
                # we haven't visited yet, so calcualte a new distance to compare
                newDistance = currentDistance + distance
                if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                    ### We either haven't got a distance for this neighbour
                    ### or the new distance is shorter, so let's update that.
                    unvisited[neighbour] = newDistance
                    previous[neighbour] = current
# =============================================================================
#       FIND IF DESTINATION NODE IS FULLY VISITED, IF NOT THEN
#       FIND NEIGHBOUR OF CURRENT NODE WITH MIN DISTANCE AND MOVE
# =============================================================================
        ## add the current place to the visited list
        visited[current] = currentDistance
        ## remove the current place from unvisited
        del unvisited[current]
        if route[-1] in visited: break
        if not unvisited: break
        ## find some new neighbours
        candidates = list()
        for new_neighbour in unvisited.items():
            # do we have a tentative distance for this neighbour?
            if new_neighbour[1]:
                # yes, add it to the candidates and sort in ascending distances
                candidates.append(new_neighbour)
                current, currentDistance = sorted(candidates, key = lambda x : x[1])[0]
        if len(candidates) == 0:
            print("We have no route from: ", route[0], " -> ",route[-1])
            return ([], -1)
            break
        # MOVE TO THE NODE WITH THE SHORTEST DISTANCE
        print("Moving to :", current)
    path = reconstructPath(route[0], route[-1], previous)
    print(path)
    # return the path taken and the shortest distance to end node.
    print(visited[route[-1]])
    return (path, visited[route[-1]])

def reconstructPath(start, end, previous_connections):
    ## reconstruct the path taken using back tracking
    path = []
    # start at the destination and work backwards
    node = end
    # since we have defined previous[start] as None we can end there.
    while previous_connections[node]:
        # append the current node to the path
        path.append(node)
        # go to the node with shortest distance from node
        node = previous_connections[node]
    # append the start node to the path for finish.
    path.append(start)
    # reverse the path taken to get path from start -> end
    path.reverse()
    return path

