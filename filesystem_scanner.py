from pathlib import Path
import ast

repo = input('Insert repo path:\n')
repo = Path(repo.strip(""))
modules = []
functions = []

if repo.exists():

    for node in repo.rglob('*.py'):
        path = node.name
        with open(node, 'r') as f:
            obj = ast.parse(f.read())
            
        for n in ast.walk(obj):
            if isinstance(n, ast.ImportFrom):
                modules.append(n.module)
            
            if isinstance(n, ast.FunctionDef):
                functions.append(n.name)
            
            
    def dictionary_constructor(path ,modules,functions):
        dependency_tree={}
        dependency_tree[path] = {
                'modules': modules,
                'function':functions
                }
        
        return dependency_tree
    dp_graph = dictionary_constructor(path, modules, functions)
    
    def dependency_graph(repository):
        nodes = set()
        edges = []

        for file_name, data in repository.items():

            # Current file becomes a node
            nodes.add(file_name)

            # Every import becomes a relationship
            for module in data["modules"]:

                if module is None:
                    continue

            # Imported module is also a node
                nodes.add(module)

            # Edge
                edges.append((file_name, module))
                
            print('Nodes')
            print('*'*60)
            for n in nodes:
                print(n)
            
            print('Edges')
            print('*'*60)
            for n,edge in edges:
                print(f'{n}--->{edge}')

        
       
        
    print(dependency_graph(dp_graph))
    def console_view():
        dp_graph = dictionary_constructor(path, modules, functions)
        print('*'*60)
        print('REPOGRAPH')
        print('*'*60)
    
        for k in dp_graph:
            print(f'Module {k}')
            print("Imports")
            print('*'*60)
            [print(module) for module in dp_graph[k].get('modules',[])]
            print(f'Module Number {len(dp_graph[k].get('modules', []))}')
    #print(ast.dump(obj, indent= 2))      

        
else:
    print('Path does not exisit.')
    
   


