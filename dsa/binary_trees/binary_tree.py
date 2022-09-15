# structure of a binary tree"


"""
key points

-> Depth of Node: 
        the length of the path from a node, n to the root node. 
        the depth of root node is 0
-> Height of Tree:
        the length of the path from n to its deepest descendant
        the height of the tree itself is the height of the root node
        the height of leaf node is always 0

Types of binary tree

-> complete binary tree
        every level except possibly the last, is completely filled 
        and all nodes in the last level are as far left as possible

-> full binary tree
        A full binary tree(sometimes referred to as a proper or plane binary tree) is a tree in which every node has either 0 or 2 children

"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tr# Time Complexity: O(n)
# Space Complexity: O(1)
def find_fixed_point_linear(A):
    for i in range(len(A)):
        if A[i] == i:
            return A[i]
    return None


# Time Complexity: O(log n)
# Space Complexity: O(1)
def find_fixed_point(A):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high)//2

        if A[mid] < mid:
            low = mid + 1
        elif A[mid] > mid:
            high = mid - 1
        else:
            return A[mid]
    return None

# Fixed point is 3:
A1 = [-10, -5, 0, 3, 7]

# Fixed point is 0:
A2 = [0, 2, 5, 8, 17]

# No fixed point. Return "None":
A3 = [-10, -5, 3, 4, 7, 9]
print("Linear Approach")
print(A1)
print(find_fixed_point_linear(A1))
print(A2)
print(find_fixed_point_linear(A2))
print(A3)
print(find_fixed_point_linear(A3))
print("Binary Search Approach")
print(A1)
print(find_fixed_point(A1))
print(A2)
print(find_fixed_point(A2))
print(A3)
print(find_fixed_point(A3))ee.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")

        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def preorder_print(self, start, traversal):
        """Root->Left->Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """Left->Root->Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """Left->Right->Root"""
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

# 1-2-4-5-3-6-7-
# 4-2-5-1-6-3-7
# 4-5-2-6-7-3-1
#               1
#           /       \  
#          2          3  
#         /  \      /   \
#        4    5     6   7 

# Set up tree:
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print("preorder:", tree.print_tree("preorder"))
print("inorder:", tree.print_tree("inorder"))
print("postorder:", tree.print_tree("postorder"))