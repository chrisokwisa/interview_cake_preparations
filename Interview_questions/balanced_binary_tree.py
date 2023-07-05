# Write a function to see if a binary tree is "superbalanced" (a new tree property we just made up)

# A tree is 'superbalanced' if the difference between the depths of any two leaf nodes is no greater than one

# A binary tree is a tree where every node has two or fewer children. The children are usually called left and right

# Here's a sample binary tree node class:

# class BinaryTreeNode(object):

#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
        
#     def insert_left(self, value):
#         self.left = BinaryTreeNode(value)
#         return self.left
    
#     def insert_right(self, value):
#         self.right = BinaryTreeNode(value)
#         return self.right
    

# Solution
# We do a depth-first walk through our tree, keeping track of the depth as we go. When we find a leaf
# we add its depth to list of depths if we haven't seen that depth already

# Each time we hit a leaf with a new depth, there are two ways that our tree might now bw balanced
#   1) There are more than 2 different leaf depths
#   2) There are exactly 2 leaf depths and they are more than 1 apart

# ======================= depth-first walk

# Depth-first search ( DFS) is a method for exploring a tree or graph. In a (DFS), you go as deep as possible
# down one path before backing up and tring a different one

# Depth-first search is like walking  through a corn maze. You explore one path,
# hit a dead end, and go back and try a  different one
# ================= Advantages:
    #  Depth-first search on a  binary tree is generally requires less memory than
        #   breath-first search

    # Depth-first search can be easily implemented with recursion

# ==================== Disadvantages:
    # A DFS doesn't necessarily find the shortestpath to a node, while breadth-first search does


def is_balanced(tree_root):
    # A tree with no nodes is superbalanced, since there are no leaves

    if tree_root is None:
        return True
    
    # We short-circuit as soon as we find more than 2
    depths = []

    # We'll treat this list as a stacj that willl sore tuples of (node, depth)
    nodes = []
    nodes.append((tree_root, 0))

    while len(nodes):
        #  Pop a node and its depth from the top of our stack
        node, depth = nodes.pop()

        #  Case: we found a leaf
        if (not node.left) and (not node.right):
            # We only care if it's a new depth
            if depth not in depths:
                depths.append(depth)

                # Two ways we might now have an unbalanced tree:
                #   1) more than 2 different leaf depths
                #   2) 2 leaf depths that are more than 1 apart
                if (len(depths) > 2) or (len(depths) == 2 and abs(depths[0] - depths[1]) > 1):
                    return False
                
        else:
            # case: this isn'ta leaf - keep stepping down
            if node.left:
                node.append((node.left, depth + 1))

            if node.right:
                nodes.append((node.right, depth + 1))

    return True
                
# Tests

class BinaryTreeNode(object):
    
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            
        def insert_left(self, value):
            self.left = BinaryTreeNode(value)
            return self.left
        
        def insert_right(self, value):
            self.right = BinaryTreeNode(value)
            return self.right
        
# =========================== Test 1
# A tree with no nodes is superbalanced, since there are no leaves

tree = BinaryTreeNode(5)
result = is_balanced(tree)
print(result)

# =========================== Test 2
# A tree with one node is also superbalanced, since the difference between
# the depths of any two leaf nodes is 0

tree = BinaryTreeNode(5)
tree.insert_left(8)
result = is_balanced(tree)
print(result)

# =========================== Test 3
# A tree with two nodes at different depths

tree = BinaryTreeNode(5)
left = tree.insert_left(8)
left.insert_left(1)
left.insert_right(2)
tree.insert_right(6)
result = is_balanced(tree)
print(result)

