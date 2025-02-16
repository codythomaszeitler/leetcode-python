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
		if not root:
			return None
		if root.val == key:
			return self.delete(root)
			
		result = self.find(root, key, None)
		if result == None:
			return root

		node, parent = result

		new_sub_tree_root = self.delete(node)
		if parent.left and parent.left.val == node.val:
			parent.left = new_sub_tree_root
		else:
			parent.right = new_sub_tree_root
		return root
	
	def delete(self, node):
		smallest_right = self.find_smallest_node(node.right)
		if not smallest_right:
			return node.left
		smallest_right.left = node.left
		return node.right

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