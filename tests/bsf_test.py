"""
Breadth-First Search Algorithm

Input: graph: Dict, start: String

1. Initialize (set->visited) with start
2. Intialize queue[start]
3. while queue is not empty
    4. node = deque the queue
    5. process(node)
    6. for each graph.get(node, [])
        7. if each is not in visted
        8. enque each
        9. add into set

"""
from collections import deque

def proccess(node: str):
    print(node,'->')
    

def bfs(graph: dict, start: str):
    visited = set([start])
    queue = deque([start])
    depth = 0

    
    while queue:
        node = queue.popleft()
        proccess(node)
        depth += 1
        for n in graph.get(node, []):
            if n not in visited:
                queue.append(n)
                visited.add(n)
    
    print(depth)
    
    
                
graph = {
    'A': ['B', 'C'],
    'B':['A', 'D'],
    'C':['A', 'E', 'F'],
    'D':['A','B'],
    'E':['C'],
    'F':['C']
}

graph_1 = {
    '''This was my test graph'''
    
}

bfs(graph=graph, start='A')