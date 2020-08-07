'''
Resouces:
https://www.annytab.com/a-star-search-algorithm-in-python/
https://www.geeksforgeeks.org/a-search-algorithm/
https://www.bogotobogo.com/python/python_PriorityQueue_heapq_Data_Structure.php
'''
import math
from collections import defaultdict
import heapq

def shortest_path(M, start, goal):
    # store the nodes and dist (f) as a min heap to easily fetch minimum
    nodes_min_heap = []
    heapq.heappush(nodes_min_heap, (0, start))
    
    # backtrack dictionary to store prev node used to backtrack and trace path
    backtrack = defaultdict()
    # distance of each node stored in a dictionary
    distance = defaultdict()
    
    backtrack[start] = None
    # storing the g distance
    distance[start] = 0
    
    while len(nodes_min_heap)>0:
        node = heapq.heappop(nodes_min_heap)
        # node[1] contains the node name and node[0] contains the f distance of node
        if node[1] == goal:
            return trace_path(backtrack, start, goal)
        
        # calculate distance of each neighbor and push it into the min_heap for next round of min distance calculation
        for neighbor in M.roads[node[1]]:
            # neighbor new_dist is the distance of the current node plus dist between curr node and neighbor
            # here since the distance between two points is a straight line, dist between them is equal to heuristic dist
            new_dist = distance[node[1]] + heuristic_dist(M,node[1],neighbor)
            
            # take minimum of the newly calc distance and any present dist
            if neighbor not in distance or new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                # f = g + h
                f = new_dist + heuristic_dist(M,goal,neighbor)
                heapq.heappush(nodes_min_heap, (f, neighbor))
                backtrack[neighbor] = node[1]
    
    return "No Path"

# backtrack and print the path
def trace_path(backtrack, start, goal):
    curr_node = goal
    path = [curr_node]
    while curr_node!=start:
        #print(curr_node)
        prev = backtrack[curr_node]
        #print(prev)
        path.append(prev)
        curr_node = prev    
    return path[::-1] 
            
# distance between two points on a coordinate system            
def heuristic_dist(M,a, b):
    p = M.intersections[a]
    q = M.intersections[b]
    return math.sqrt(((p[0]-q[0])**2) + ((p[1]-q[1])**2))