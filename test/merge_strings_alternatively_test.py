import unittest
from src.merge_strings_alternatively import Solution

class MergeStringsAlternativelyTest(unittest.TestCase):
	def test_merge_strings_alternatively(self):
		word1 = "abc"
		word2 = "pqr"

		test_object = Solution()
		expected = "apbqcr"
		self.assertEqual(expected, test_object.mergeAlternately(word1, word2))
	
	def test_2(self):
		word1 = "ab"
		word2 = "pqrs"

		test_object = Solution()
		expected = "apbqrs"
		self.assertEqual(expected, test_object.mergeAlternately(word1, word2))

	def test_3(self):
		word1 = "abcd"
		word2 = "pq"

		test_object = Solution()
		expected = "apbqcd"
		self.assertEqual(expected, test_object.mergeAlternately(word1, word2))
	
	def test_4(self):
		word1 = "a"
		word2 = "b"
  
		test_object = Solution()
		expected = "ab"
		self.assertEqual(expected, test_object.mergeAlternately(word1, word2))

	def test_5(self):
		word1 = ""
		word2 = "b"
  
		test_object = Solution()
		expected = "b"
		self.assertEqual(expected, test_object.mergeAlternately(word1, word2))

	def test_6(self):
		word1 = "a"
		word2 = ""
  
		test_object = Solution()
		expected = "a"
		self.assertEqual(expected, test_object.mergeAlternately(word1, word2))

	def test_7(self):
		word1 = ""
		word2 = ""
  
		test_object = Solution()
		expected = ""
		self.assertEqual(expected, test_object.mergeAlternately(word1, word2))

	def test_8(self):
		word1 = None
		word2 = "b"
  
		test_object = Solution()
		expected = "b"
		self.assertEqual(expected, test_object.mergeAlternately(word1, word2))

	def test_9(self):
		word1 = "a" 
		word2 = None
  
		test_object = Solution()
		expected = "a"
		self.assertEqual(expected, test_object.mergeAlternately(word1, word2))