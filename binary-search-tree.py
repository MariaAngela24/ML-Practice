#Given a node, find the node with the next largest value
#Assume a valid binary search tree.  Assume node has the 
#methods left, right, and parent
def find_leftmost(node):
    while node.left:
        node = node.left
    return node


def find_next_node(node):
    if node.right is not None:
        node = node.right
        find_leftmost(node)
        
    else:
        while node.parent < node:
            node = node.parent
        return node.parent
            
            
find_next_node(7)  
find_next_node(2)
