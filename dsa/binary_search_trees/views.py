class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
    
    def topView(self):
        q = []
        q.append((self.root, 0))
        hd = 0
        l = 0
        r = 0

        left = []
        right = []

        while len(q) > 0:
            node, hd = q[0]

            if hd < l:
                left.append(node.data)
                l = hd
            elif hd > r:
                right.append(node.data)
                r = hd
            
            if node.left != None:
                q.append((node.left, hd - 1))
            if node.right != None:
                q.append((node.right, hd + 1))
            q.pop(0)

        while len(left) > 0:
            x = left.pop()
            print(x, end=" ")

        print(self.root.data, end=" ")

        for x in right:
            print(x, end=" ")

    def leftView(self):
        if not self.root:
            return
        t = self.root
        while t:
            print(t.data, end=" ")
            t = t.left
    
    def rightView(self):
        if not self.root:
            return
        t = self.root
        while t:
            print(t.data, end=" ")
            t = t.right

if __name__ == "__main__":
    t = BST()
    t.root = Node(1)
    t.root.left = Node(2)
    t.root.right = Node(3)
    t.root.left.right = Node(4)
    t.root.left.right.right = Node(5)
    t.root.left.right.right.right = Node(6)
    t.topView()
    print()
    t.leftView()
    print()
    t.rightView()



"""

        1
      /   \
    2       3
      \   
        4  
          \
            5
             \
               6 


"""