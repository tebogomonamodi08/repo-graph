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
    
    
                
graph = {
    'A': ['B', 'C'],
    'B':['A', 'D'],
    'C':['A', 'E', 'F'],
    'D':['A','B'],
    'E':['C'],
    'F':['C']
}


from collections import deque

def bfs_search(graph, start, depth = 0):
    if start in graph:
        visted = set([start]) #we use this to stop cyclic traversal
        queue = deque([(start,depth)])
        
        
        while queue:
            current_node, current_depth  = queue.popleft()
            print(current_node, current_depth)
           
            
            for n in graph[current_node]:
                if n not in visted:
                    queue.append((n, current_depth+1))
                    visted.add(n)
                    
                    
    else:
        print('Node does not exist')
    
    print(queue)

bfs_search(graph, 'A')
        