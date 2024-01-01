class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
    
    def search(self,data):
        if self.key == data:
            print('Node is found')
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else: 
                print('Node is not found')
        else:
            if self.rchild:
                self.rchild.search(data)
            else: 
                print('Node is not found')
    
    def preOrder(self):
        print(self.key, end=' ')
        if self.lchild:
            self.lchild.preOrder()
        if self.rchild:
            self.rchild.preOrder()
    
    def inOrder(self):
        if self.lchild:
            self.lchild.inOrder()
        print(self.key, end=' ')
        if self.rchild:
            self.rchild.inOrder()
    
    def postOrder(self):
        if self.lchild:
            self.lchild.postOrder()
        if self.rchild:
            self.rchild.postOrder()
        print(self.key, end=' ')

    def delete(self, data, curr):
        if self.key is None:
            print('tree is empty')
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data, curr)
            else:
                print('node is not present')
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data, curr)
            else:
                print('node is not present')
        else:
            if self.lchild is None:
                temp = self.rchild
                if data == curr:
                    self.key=temp.key
                    self.lchild=temp.lchild
                    self.rchild=temp.rchild
                    temp = None
                    return
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                if data == curr:
                    self.key=temp.key
                    self.lchild=temp.lchild
                    self.rchild=temp.rchild
                    temp = None
                    return 
                self = None
                return temp 
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key,curr)
        return self
    
    def min_node(self):
        current = self
        while current.lchild:
            current = current.lchild
        print('node with min key is: ', current.key)

    def max_node(self):
        current = self
        while current.rchild:
            current = current.rchild
        print('node with max key is: ', current.key)


def count(node):
    if node is None:
        return 0
    return 1+count(node.lchild)+count(node.rchild)
root = BST(10)
lst1 = [11,12]
for i in lst1:
    root.insert(i)
print(count(root))
if count(root) > 1:
    root.delete(10, root.key)
else:
    print("can'nt delete ")
root.preOrder()
print()
root.min_node()
root.max_node()