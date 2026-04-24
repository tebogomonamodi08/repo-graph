

'''
Overview: A failure aware and deterministic system that takes repo tree represented in JSON
and returns a dictionary of nodes and there respective relationships.

input:
{
    repo_name: repo,
    files: [
        {'file_name', 'content', 'size', 'path'}
    ]
}

output: 
 {
     nodes: []
     edges: []
 }

'''


from ingestion_engine import ingest
import os

path = r'C:\Users\Tebogo\OneDrive - Linkfields innovations\Desktop\observability_tool\test\test_repo'
ingested_repo, trace = ingest(path)

#\\observability_tool\\test\\test_repo\\models\\train.py

#Constraits: Each node has to be unique
#system
#split the relative path -> list e.g [observability_tool, test, test_repo, models, train.py]

#output : {edges: [type: folder, name: observability_tool, contains: test]

#if list<2->skip add to set
#else:
#iterate-> element if not in set add
#if os.path.split == '' is file, else folder, name: list_element, contains:list+1

'''
Initialize:
    set = None
    graph = {}
    current_path = None
    prev_path = None
    list = split(input)
    for each part:
        if current path:
            current_path = part
        else:
            current_path = current_path + \ + part
        set.add(current_path)
        if prev_path:
            graph[edges: {prev:current_path}]
        prev_path = current_path



'''

node = set()
graph = {}
edges = []

for f in ingested_repo['files']:
    current_path = None
    prev_path = None
    parts = f['relative_path'].split(os.sep)
    for part in parts:
        if current_path:
            current_path = part
        else:
            current_path = f'{current_path}/{part}'
        node.add(current_path)
        if prev_path:
            edges.append((prev_path,current_path))
        prev_path = current_path
        
        
        
        graph= {
            'nodes' : node,
            'edges' : edges
            
        }
    

print(graph)

                











