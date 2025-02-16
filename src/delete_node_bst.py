# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
	def deleteNode(self, root, key):
		"""
		:type root: Optional[TreeNode]
		:type key: int
		:rtype: Optional[TreeNode]
		"""
		# I really 
		result = self.find(root, key, None)
		if result == None:
			return root

		node, parent = result

		smallest_right = self.find_smallest_node(node.right)
		if smallest_right == None:
			if not parent: 
				return node.left
			parent.left = node.left
			return parent

		smallest_right.left = node.left
		if parent == None:
			return node.right
		else:
			parent.left = node.right
			return root

	def find(self, node, target, parent):
		if node == None:
			return None
		if target == node.val:
			return node, parent
		if node.val < target:
			return self.find(node.right, target, node)
		else:
			return self.find(node.left, target, node)

	def find_smallest_node(self, node):
		if node == None:
			return node
		if node.left == None:
			return node
		return self.find_smallest_node(node.left)