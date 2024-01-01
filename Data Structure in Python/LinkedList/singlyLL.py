
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_LL(self):
        if self.head is None:
            print('List is empty')
        else:
            n = self.head
            while n is not None:
                print(n.data, '--->', end=' ')
                n = n.ref
    
    def add_beign(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    
    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print('Item not Found')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    def add_before(self, data, x):
        if self.head is None:
            print('List is Empty')
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n.ref = n
        if n is None:
            print('Node is not Found')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print('list is not empty')

    def delete_begin(self):
        if self.head is None:
            print('list is empty')
            return
        self.head = self.head.ref
    
    def delete_end(self):
        if self.head is None:
            print('list is empty')
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None
    
    def delete_by_value(self, x):
        if self.head is None:
            print('list is empty')
            return
        if x == self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print('Node is not present')
        else:
            n.ref = n.ref.ref
        

LL1 = LinkedList()
LL1.add_beign(10)
LL1.add_beign(20)
LL1.add_beign(30)
LL1.delete_by_value(20)
LL1.delete_by_value(30)
LL1.print_LL()
