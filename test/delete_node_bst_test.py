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
	
	def test_3(self):
		root = list_to_binary_tree([5,3,6,2,4,None,7])
		test_object = Solution()
		actual = test_object.deleteNode(root, 7)
		expected = list_to_binary_tree([5,3,6,2,4])
		self.assertEqual(actual, expected)
	
	def test_4(self):
		root = list_to_binary_tree([4,None,7,6,8,5,None,None,9])
		test_object = Solution()
		actual = test_object.deleteNode(root, 7)
		expected = list_to_binary_tree([4, None, 8, 6, 9, 5])
		self.assertEqual(actual, expected)

	def test_5(self):
		root = list_to_binary_tree([2,1,3])
		test_object = Solution()
		actual = test_object.deleteNode(root, 1)
		expected = list_to_binary_tree([2, None, 3])
		self.assertEqual(expected, actual)
	
	def test_6(self):
		root = list_to_binary_tree([])
		test_object = Solution()
		actual = test_object.deleteNode(root, 0)
		self.assertIsNone(actual)
	
	def test_7(self):
		root = list_to_binary_tree([5,3,6,2,4,None,7])

		test_object = Solution()
		actual = test_object.deleteNode(root, 11)
		self.assertEqual(actual, root)
		pass