#Given the root to a binary tree, 
# implement serialize(root), 
# which serializes the tree into a string, 
# and deserialize(s), which deserializes the string back into the tree.


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deserialize(data):
    vals = data.split(',')
    idx = 0
    def build():
        nonlocal idx  # FIX 1
        if vals[idx] == 'NULL':
            idx += 1
            return None
        node = Node(vals[idx])
        idx += 1
        node.left = build()
        node.right = build()
        return node
    return build()  # FIX 2

def serialize(root):
    vals = []
    def preorder(node):
        if node == None:
            vals.append('NULL')
            return  # FIX 3
        vals.append(node.val)
        preorder(node.left)
        preorder(node.right)
    preorder(root)
    return ','.join(vals)

# Test
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
print("Test passed!")