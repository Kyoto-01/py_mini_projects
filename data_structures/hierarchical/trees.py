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
		if node:
			return 1 + max(self.height(node.left_child), self.height(node.right_child))
		return 0

	def depth(self, node: 'Node' = ROOT, root: 'Node' = ROOT):
		if root == ROOT:
			root = self.root
		if root:
			if node is root:
				return 1
			depth = max(self.depth(node, root.left_child), self.depth(node, root.right_child))
			if depth > 0:
				return 1 + depth
		return 0

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

	def formated_print(self, root: 'Node' = ROOT, child_side: str = ''):
		if root == ROOT:
			root = self.root
		if root:
			print(' ' * self.depth(root), child_side, root, sep='')
			self.formated_print(root.left_child, 'l')
			self.formated_print(root.right_child, 'r')


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

	def main_return(self, root: 'Node'):
		return root

	def insert(self, data: object, root: 'Node' = ROOT):
		if root == ROOT:
			root = self.root = self.insert(data, self.root)
		else:
			if root is None:
				return Node(data)
			if data < root.data:
				root.left_child = self.insert(data, root.left_child)
			if data > root.data:
				root.right_child = self.insert(data, root.right_child)

		return self.main_return(root)

	def remove(self, key: object, root: 'Node' = ROOT):
		if root == ROOT:
			root = self.root = self.remove(key, self.root)
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

		return self.main_return(root)

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


class AvlTree(BinarySearchTree):

	def __init__(self, root: 'Node' = None):
		super().__init__(root)

	def main_return(self, root: 'Node'):
		return self.balance(root)

	def get_balance_factor(self, root: 'Node' = ROOT):
		if root == ROOT:
			root = self.root
		if root is None:
			return 0
		return self.height(root.left_child) - self.height(root.right_child)

	def balance(self, root: 'Node' = ROOT):
		if root == ROOT:
			root = self.root

		bf = self.get_balance_factor(root)
		lbf = self.get_balance_factor(root.left_child)
		rbf = self.get_balance_factor(root.right_child)
		
		# left-left insert --> simple rotate to "right"
		if bf > 1 and lbf >= 0:
			return self.__right_rotate(root)
		# right-right insert --> simple rotate to "left"
		if bf < -1 and rbf <= 0:
			return self.__left_rotate(root)
		# left-right insert --> double rotate to "left" and after "right"
		if bf > 1 and lbf < 0:
			root.left_child = self.__left_rotate(root.left_child)
			return self.__right_rotate(root)
		# right-left insert --> double rotate to "right" and before "left"
		if bf < -1 and rbf > 0:
			root.right_child = self.__right_rotate(root.right_child)
			return self.__left_rotate(root)

		return root

	def __right_rotate(self, root: 'Node'):
		temp = root
		root = temp.left_child
		temp.left_child = root.right_child
		root.right_child = temp
		return root

	def __left_rotate(self, root: 'Node'):
		temp = root
		root = temp.right_child
		temp.right_child = root.left_child
		root.left_child = temp
		return root
