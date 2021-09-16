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

    # TODO debug the method below
    def depth(self, node: 'Node' = ROOT, root: 'Node' = ROOT, depth: int = 1):
        if root == ROOT:
            root = self.root
        if (root is None) or (node == ROOT):
            return 0
        if node is root:
            return depth
        depth = self.depth(node, root.left_child, depth + 1)
        if depth == 0:
            depth = self.depth(node, root.right_child, depth + 1)
        return depth

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

    def __pre_order_nav(self, root: 'Node' = ROOT):
        if root:
            print(root, end='; ')
            self.__pre_order_nav(root.left_child)
            self.__pre_order_nav(root.right_child)
            
    def __in_order_nav(self, root: 'Node' = ROOT):
        if root:
            self.__in_order_nav(root.left_child)
            print(root, end='; ')
            self.__in_order_nav(root.right_child)
            
    def __post_order_nav(self, root: 'Node' = ROOT):
        if root:
            self.__post_order_nav(root.left_child)
            self.__post_order_nav(root.right_child)
            print(root, end='; ')
            
    def pre_order_nav(self, root: 'Node' = ROOT):
        if root == ROOT:
            root = self.root
        self.__pre_order_nav(root)
        print()
            
    def in_order_nav(self, root: 'Node' = ROOT):
        if root == ROOT:
            root = self.root
        self.__in_order_nav(root)
        print()
            
    def post_order_nav(self, root: 'Node' = ROOT):
        if root == ROOT:
            root = self.root
        self.__post_order_nav(root)
        print()
            
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
    print('''*-- Options --*
<----------------------------------------->
[NAVIGATION] [1]
    --> pre-order (1)
    --> in-order (2)
    --> post-order (3)
    --> left-border (4)
    --> right-border (5)
    --> formated-tree-print (6)
[OPERATIONS] [2]
    --> insert (1)
    --> remove (2)
    --> search (3)
[DATAS] [3]
    --> min-child (1)
    --> max-child (2)
    --> count (3)
    --> height (4)
    --> depth (5)
[SAIR] [x]
<----------------------------------------->
        Example:
            option >> 1 2
            (makes a in-order navigation)
<----------------------------------------->\n''')

    while True:
    
        try:
            option = input('option >> ').split(maxsplit=1)
            group, op = option[0], option[1]
            
        except IndexError:
            if len(option) > 0:
                if option[0] == 'x':
                    print('exiting...')
                    break
            
        else:
            if group == '1':
                if op == '1':
                    nums.pre_order_nav()
                elif op == '2':
                    nums.in_order_nav()
                elif op == '3':
                    nums.post_order_nav()
                elif op == '4':
                    nums.left_border_nav()
                elif op == '5':
                    nums.right_border_nav()
                elif op == '6':
                    pass
                
            elif group == '2':
                if op == '1':
                    data = int(input('To insert -> '))
                    nums.insert(data)
                elif op == '2':
                    data = int(input('To remove -> '))
                    nums.remove(data)
                elif op == '3':
                    data = int(input('To search -> '))
                    nums.search(data)
                    
            elif group == '3':
                if op == '1':
                    print(nums.min_child())
                elif op == '2':
                    print(nums.max_child())
                elif op == '3':
                    print(nums.count())
                elif op == '4':
                    data = int(input('Node ->'))
                    print(nums.height(nums.search(data)))
                elif op == '5':
                    data = int(input('Node ->'))
                    print(nums.depth(nums.search(data)))
                    
