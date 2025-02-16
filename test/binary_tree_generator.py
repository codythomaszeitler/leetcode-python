class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
	
	def __eq__(self, other):
		if not isinstance(other, TreeNode):
			return NotImplemented
		return other.left == self.left and other.right == self.right and  other.val	== self.val

	def __ne__(self, other):
		x = self.__eq__(other)
		if x is not NotImplemented:
			return not x
		return NotImplemented

def list_to_binary_tree(lst):
	if not lst:
		return None

	root = TreeNode(val=lst[0])  # The first element is the root
	queue = [root]  # Queue to help assign left and right children
	idx = 1  # Start from the second element in the list

	while queue:
		current = queue.pop(0)  # Get the next node from the queue

		# Assign left child if there's a next element
		if idx < len(lst):
			value = lst[idx]
			if value != None:
				current.left = TreeNode(val=value)
				queue.append(current.left)  # Add left child to the queue
			idx += 1

		# Assign right child if there's a next element
		if idx < len(lst):
			value = lst[idx]
			if value != None:
				current.right = TreeNode(val=lst[idx])
				queue.append(current.right)  # Add right child to the queue
			idx += 1

	return root