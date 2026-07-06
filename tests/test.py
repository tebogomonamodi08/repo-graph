import ast

code  = """
class Dog:
    def __init__(self, legs=4):
        continue

"""



tree = ast.parse(code)



print(ast.dump(tree, indent= 2))