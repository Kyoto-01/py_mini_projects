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

    def count(self, root: 'Node' = ROOT):
        if root == ROOT:
            root = self.root
        if root is None:
            return 0

        return 1 + self.count(root.left_child) + self.count(root.right_child)

    def height(self, node: 'Node' = ROOT):
        if node == ROOT:
            node = self.root
        if (node is None) or (not node.left_child and not node.right_child):
            return 0
        left_height = 1 + self.height(node.left_child)
        right_height = 1 + self.height(node.right_child)

        return max(left_height, right_height)
        
    def depth(self, node: 'Node' = ROOT):
        if node == ROOT:
            node = self.root
        if node is None:
            return 0
        return self.height() - self.height(node)

    def data_height(self, data: object):
        find = self.search(data)
        if find:
            return self.depth(find)

    def data_depth(self, data: object):
        find = self.search(data)
        if find:
            return self.depth(find)

    def search(self, key: object, root: 'Node' = ROOT):
        if root == ROOT:
            root = self.root
        if root is None:
            return None
        if key == root.data:
            return root
        find = self.search(key, root.left_child)
        if find is None:
            find = self.search(key, root.right_child)

        return find

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

    def min_child(self, root: 'Node' = ROOT):
        if root == ROOT:
            root = self.root
        if root:
            while root.left_child:
                root = root.left_child

        return root

    def max_child(self, root: 'Node' = ROOT):
        if root == ROOT:
            root = self.root
        if root:
            while root.right_child:
                root = root.right_child

        return root
        
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
            self.root = self.remove(key, self.root)
        else:
            if root is None:
                return None
            if key < root.data:
                root.left_child = self.remove(key, root.left_child)
            elif key > root.data:
                root.right_child = self.remove(key, root.right_child)
            else:
                if not root.left_child:
                    return root.right_child
                if not root.right_child:
                    return root.left_child

                min_right_child = self.min_child(root.right_child)
                root.data = min_right_child.data
                root.right_child = self.remove(min_right_child.data, root.right_child)

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
    # * TESTS *

    # ** initial tree: **
    #
    #         6
    #        / \
    #      2    8
    #     / \   /\
    #   1    4 7  9
    #  /    / \    \
    # 0    3   5    10
    #
        
    nums = BinarySearchTree()
    nums.insert(6)
    nums.insert(2)
    nums.insert(1)
    nums.insert(4)
    nums.insert(0)
    nums.insert(3)
    nums.insert(5)
    nums.insert(8)
    nums.insert(7)
    nums.insert(9)
    nums.insert(10)

    # ** menu **
    print('''*-- Options --*\n
[NAVIGATION] [1]
    --> pre-order (1)
    --> in-order (2)
    --> post-order (3)
    --> left-border (4)
    --> right-border (5)
[OPERATIONS] [2]
    --> insert (1)
    --> remove (2)
    --> search (3)
[DATAS] [3]
    --> min-child (1)
    --> max-child (2)
    --> count (3)
    --> height (4)
    --> data-height (5)
    --> depth (6)
    --> data-depth (7)''')
