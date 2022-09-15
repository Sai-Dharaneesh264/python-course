from queue import Queue

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree(object):

    def __init__(self, data):
        self.root = Node(data)


    def levelorder_print(self):
        if self.root is None:
            return
        queue = Queue()
        queue.enqueue(self.root)
        traversal = ""
        while queue.size() > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()
            
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
            print('size = ', queue.size())
            print(node.data, end="-*-")
        return traversal


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
print(tree.levelorder_print())