'''
This module is responsible for transforming the output of the graph engine to adjecency list and traversing it
the output from graph_engine(a dictionary of nodes and edges)
then extracting insights from the structure(structural analysis for repo structure). 

Flow:
Input(graph_engine) -> Data Transformation -> BFS Algorithm -> Extract Depth, Hotspot

Performace:
For this module I used Breadth-first algorithm to traverse each node in the adjecency list. I will
evaluate the complexity of this decison later on

Arguments:

1. Why do these Metrics matter honestly?
 -Depth
 -Hotspot


'''

from graph_engine import create_graph
from collections import deque

graph = create_graph()


'''
data transformation:
#create dictionary with keys from graph 

'''

def graph_transformer(graph: dict)->dict:
    '''
    This module tranforms a dictionary containing nodes and edges into an adjacency list that a breadth-first 
    search algorithm can take an an output
    input: {nodes[], edges[]}
    
    output: {
        a: [],
    }
    
    '''
    
    adjencency_list = {}
    for node in graph.get('nodes', []):
        adjencency_list[node.get('id')] = []
    
    for edge in graph.get('edges',[]):
        source = edge.get('source')
        target = edge.get('target')
    
        if source in adjencency_list:
            adjencency_list[source].append(target)
    
    return adjencency_list


adj_list = graph_transformer(graph)


def traverse_graph(adj_list: dict, start, depth = 0)->dict:
    '''
    This function traverses the tree level to level and derives metrics: depth, hotspots: top tree and number of folders
    and files
    '''
    start = adj_list[0]
    visted = set([start])
    queue = deque([(start, depth)])
    depth_map = {
        start : 0,
    }
    
    while queue:
        current_node, current_depth = queue.popleft()
        #node exection
        
        for n in adj_list[current_node]:
            if n not in visted:
                queue.append((n,current_depth+1))
                depth_map[n] = depth + 1
                visted.add(n)
        
    return depth_map
    

    
    




    

    


    


        
    
