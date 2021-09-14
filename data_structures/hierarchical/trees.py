class Node:
    
    def __init__(self, data: object, left_child: 'Node' = None, right_child: 'Node' = None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child
    
    def __str__(self):
        return str(self.data)


ROOT = 'root'


class BinaryTree:
    
    def __init__(self, root: 'Node' = None):
        self.root = root
        
    def pre_order_nav(self, root: 'Node' = ROOT):
        if root == ROOT:
            root = self.root
        if root:
            print(root, end='; ')
            self.pre_order_nav(root.left_child)
            self.pre_order_nav(root.right_child)
            
    def in_order_nav(self, root: 'Node' = ROOT):
        if root == ROOT:
            root = self.root
        if root:
            self.in_order_nav(root.left_child)
            print(root, end='; ')
            self.in_order_nav(root.right_child)
            
    def post_order_nav(self, root: 'Node' = ROOT):
        if root == ROOT:
            root = self.root
        if root:
            self.post_order_nav(root.left_child)
            self.post_order_nav(root.right_child)
            print(root, end='; ')
            
    def left_border_nav(self, root: 'Node' = ROOT):
        if root == ROOT:
            root = self.root
        while root:
            print(root)
            root = root.left_child
    
    def right_border_nav(self, root: 'Node' = ROOT):
        if root == ROOT:
            root = self.root
        while root:
            print(root)
            root = root.right_child
            
            
class BinarySearchTree(BinaryTree):
    
    def __init__(self, root: 'Node' = None):
        super().__init__(root)
        
    def insert(self, data: object, root: 'Node' = ROOT):
        if root == ROOT:
            self.root = self.insert(data, self.root)
        else:
            if root is None:
                return Node(data)
            if data < root.data:
                root.left_child = self.insert(data, root.left_child)
            if data > root.data:
                root.right_child = self.insert(data, root.right_child)
                
        return root 
    
    def remove(self, key: object, root: 'Node' = ROOT):
        if root == ROOT:
            root = self.root
        if root is None:
            return root
        if key < root.data:
            root.left_child = self.remove(key, root.left_child)
        elif key > root.data:
            root.right_child = self.remove(key, root.right_child)
        else:
            if not root.left_child:
                return root.right_child
            if not root.right_child:
                return root.left_child

            actual = root.right_child
            while actual.left_child:
                actual = actual.left_child
            root.data = actual.data
            root.right_child = self.remove(actual.data, root.right_child)
        return root

    def search(self, key: object):
        pass
        
        
if __name__ == '__main__':
    
    #         6
    #      2
    #   1     4
    # 0      3  5
        
    nums = BinarySearchTree()
    nums.insert(6)
    nums.insert(2)
    nums.insert(1)
    nums.insert(4)
    nums.insert(0)
    nums.insert(3)
    nums.insert(5)

    nums.in_order_nav()
    print()

    nums.remove(5)
    nums.in_order_nav()
    print()

    nums.remove(1)
    nums.in_order_nav()
    print()
    
