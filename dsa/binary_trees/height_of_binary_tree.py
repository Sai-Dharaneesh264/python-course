class Stack(object):
    def __init__(self):
        self.items = []
    
    def __len__(self):
        return self.size()
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def __str__(self):
        s = ""
        for i in range(len(self, items)):
            s += str(self.items[i].value) + "-"
        return s

class Queue(object):
    def __init__(self):
        self.items = []
    
    def __len__(self):
        return self.size()
    
    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
           return self.items.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1].data


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, data):
        self.root = Node(data)
    
    def levelorder_print(self):
        start = self.root
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)
        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal

    def reverse_levelorder_print(self):
        start = self.root
        if start is None:
            return
        queue = Queue()
        stack = Stack()
        queue.enqueue(start)
        traversal = ""
        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        
        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.data) + "-"
        
        return traversal

    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)

    def size(self, node):
        if node is None:
            return 0
        return 1 + self.size_(node.left) + self.size_(node.right)
    
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
node = tree.root.left.right = Node(5)
print(tree.levelorder_print())
print(tree.reverse_levelorder_print())
print(tree.height(tree.root))