class Node:
    
    def __init__(self, data: object, left_child: 'Node' = None, right_child: 'Node' = None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child
    
    def __str__(self):
        return str(self.data)


ROOT = 'root'


class BinaryTree:
    
    # TODO add method to count nodes in tree
    
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
    
    # TODO add methods to find the min and the max childs 
    
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

    def search(self, key: object, root: 'Node' = ROOT):
        if root == ROOT:
            root = self.root
        if root is None:
            return root
        if key < root.data:
            return self.search(key, root.left_child)
        if key > root.data:
            return self.search(key, root.right_child)
        return root
        
        
        
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

    # remove tests
    nums.remove(5)
    nums.in_order_nav()
    print()

    nums.remove(1)
    nums.in_order_nav()
    print()
    
    nums.remove(3)
    nums.in_order_nav()
    print()
    
    # search tests
    print(nums.search(0))
    print(nums.search(2))
    print(nums.search(4))
    print(nums.search(6))
    
    print(nums.search(5))
    print(nums.search(1))
    print(nums.search(3))
    print(nums.search(100))
    
