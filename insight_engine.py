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

graph = create_graph()


'''
data transformation:
#create dictionary with keys from graph 

'''
for node in graph.get('nodes', []):
    print(node.get('label'))
        
    
