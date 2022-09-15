class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    def insert_helper(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        self.insert(self.root, data)

    def insert(self, cur, data):
        if cur.data < data:
            if cur.right:
                self.insert(cur.right, data)
            else:
                cur.right = Node(data)
        else:
            if cur.left:
                self.insert(cur.left, data)
            else:
                cur.left = Node(data)

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data, end="-")
        self.inorder(node.right)
    
    def search(self, find_val):
        return self.search_value(self.root, find_val)
    
    def search_value(self, cur, find_val):
        if cur:
            if cur.data == find_val:
                return True
            elif cur.data > find_val:
                return self.search_value(cur.left, find_val)
            else:
                return self.search_value(cur.right, find_val)
        return False

    def is_bst_satisified(self):
        def helper(node):
            if not node:
                return True
            value = node.data
            if node.left and node.left.data > value:
                return False
            if node.right and node.right.data < value:
                return False
            return helper(node.right) and helper(node.left)
        return helper(self.root)


l = BST()
root = l.root
l.insert_helper(1)
l.insert_helper(3)
l.insert_helper(4)
l.insert_helper(2)
print('inorder')
l.inorder(l.root)
print()
print(l.search(5))
print(l.is_bst_satisified())