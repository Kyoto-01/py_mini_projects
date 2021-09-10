class Node:
    
    def __init__(self, data: object, left_child: 'Node' = None, right_child: 'Node' = None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child
    
    def __str__(self):
        return str(self.data)


class BinaryTree:
    
    ROOT = 'root'
    
    def __init__(self, root: 'Node' = None):
        self.root = root
        
    def pre_order_nav(self, root: 'Node' = ROOT):
        if root == self.ROOT:
            root = self.root
        if root:
            print(root, end='; ')
            self.pre_order_nav(root.left_child)
            self.pre_order_nav(root.right_child)
            
    def in_order_nav(self, root: 'Node' = ROOT):
        if root == self.ROOT:
            root = self.root
        if root:
            self.in_order_nav(root.left_child)
            print(root, end='; ')
            self.in_order_nav(root.right_child)
            
    def post_order_nav(self, root: 'Node' = ROOT):
        if root == self.ROOT:
            root = self.root
        if root:
            self.post_order_nav(root.left_child)
            self.post_order_nav(root.right_child)
            print(root, end='; ')
            
    def left_border_nav(self, root: 'Node' = ROOT):
        if root == self.ROOT:
            root = self.root
        while root:
            print(root)
            root = root.left_child
    
    def right_border_nav(self, root: 'Node' = ROOT):
        if root == self.ROOT:
            root = self.root
        while root:
            print(root)
            root = root.right_child
            
            
class BinarySearchTree(BinaryTree):
    
    def __init__(self, root: 'Node' = None):
        super().__init__(root)
        
    def insert(self, data: object, root: 'Node' = BinaryTree.ROOT):
        if root == BinaryTree.ROOT:
            root = self.root
            
        new_child = Node(data)
        if not root:
            self.root = new_child
        elif data > root.data:
            if not root.right_child:
                root.right_child = new_child
            else:
                self.insert(data, root.right_child)
        elif data < root.data:
            if not root.left_child:
                root.left_child = new_child
            else:
                self.insert(data, root.left_child)
    
    def remove(self, key: object):
        pass
    
    def search(self, key: object):
        pass
        
        
if __name__ == '__main__':
    
    #         5
    #      2
    #   1     4
    #0      3
        
    nums = BinarySearchTree()
    nums.insert(5)
    nums.insert(2)
    nums.insert(1)
    nums.insert(4)
    nums.insert(0)
    nums.insert(3)
    
    nums.pre_order_nav()
    print()
    nums.in_order_nav()
    print()
    nums.post_order_nav()
    print()
    