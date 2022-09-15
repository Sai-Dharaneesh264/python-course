class Node:
    def __init__(self, data)
        self.data = data
        self.next = None
        self.prev = None


class CircularDoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def prepend(self, data):
        new_node = Node(data)
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        self.tail.next = self.head
        self.head.prev = self.tail

    def insert_in_middle(self, prev_node, data):
        if prev_node is None:
            print("Mentioned node doesn't exist")
            return
        
        next_node = prev_node.next
        new_node = Node(data)
        new_node.next = next_node
        new_node.prev = next_node.prev
        prev_node.next = new_node
        next_node.prev = new_node
        
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        last_node = self.head
        while last_node.next != self.head:
            last_node = last_node.next
        
        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.head
        self.head.prev = new_node
        self.tail = new_node

    def print_list(self):
        if self.head is None:
            print("the linkedList does not exists")
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.data)
                if (temp_node == self.tail):
                    break
                temp_node = temp_node.next
    
    def print_reverse_list(self):
        if self.head is None:
            print("the linkedlist does not exists")
        else:
            temp_node = self.tail
            while temp_node:
                print(temp_node.data)
                if temp_node == self.head:
                    break
                temp_node = temp_node.prev
    

    def delete_first_node(self):
        if self.head is None:
            return
        elif self.head.next == self.tail.next:
            self.head = self.tail = 
            return
        elif self.head is not None:
            next_node = self.head.next
            next_node.prev = None
            self.head = next_node
            self.tail.next = self.head
            self.head.prev = self.tail
            return
        
    def delete_in_middle(self, value):
        if self.head is None:
            return
        temp_node = self.head
        found = False

        while temp_node:
            if temp_node.data == value:
                found = True
                break
            temp_node = temp_node.next
        if found:
            prev_node = temp_node.prev
            next_node = temp_node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            return
        else:
            print("Element not found")
        
    def delete_node_at_end(self):
        if self.head is None:
            return
        elif self.head.next == self.tail.next:
            self.head = self.tail = None
            return
        else:
            temp_node = self.head
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            self.tail = temp_node
            temp_node.next = None
            self.tail.next = self.head
            self.head.prev = self.tail
            return



