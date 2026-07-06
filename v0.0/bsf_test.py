'''
def number_of_nodes(node):
    right, left = 0
    if node is Node:
        return 0
    
    right+=1
    left+=1
    return sum(right,left) + number_of_nodes(right) + number_of_node(left)


'''
