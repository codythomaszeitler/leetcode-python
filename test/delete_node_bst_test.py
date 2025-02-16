import unittest
from binary_tree_generator import list_to_binary_tree
from src.delete_node_bst import Solution

class DeleteNodeBst(unittest.TestCase):
	
	def test_1(self):
		root = list_to_binary_tree([5,3,6,2,4,None,7])

		test_object = Solution()
		expected = list_to_binary_tree([5,4,6,2,None,None,7])
		actual = test_object.deleteNode(root, 3)
		self.assertEqual(actual, expected)
	
	def test_2(self):
		root = list_to_binary_tree([0])
		test_object = Solution()
		actual = test_object.deleteNode(root, 0)
		self.assertIsNone(actual)
  