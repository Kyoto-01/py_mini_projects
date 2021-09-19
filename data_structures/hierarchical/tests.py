from trees import *


# * TESTS *

# ** initial tree: **
#
#         3
#        / \
#      1     7
#     / \ 	 / \
#    0   2  5    9
#          / \  / \
#         4  6  8 10
#

nums = AvlTree()
for n in range(11):
	nums.insert(n)

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
--> balance-factor (6)
[SAIR] [x]
<----------------------------------------->
	Example:
		option >> 1 2
		(makes a in-order navigation)
<----------------------------------------->\n''')

while True:
	option = []
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
				nums.formated_print()
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
			elif op == '6':
				print(nums.get_balance_factor())
