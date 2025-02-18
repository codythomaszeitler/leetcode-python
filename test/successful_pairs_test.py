
import unittest
from src.successful_pairs import Solution

class SuccessfulPairsTest(unittest.TestCase):
	def test_1(self):
		spells = [5, 1, 3]
		potions = [1, 2, 3, 4, 5]

		test_object = Solution()
	
		expected = [4, 0, 3]
		actual = test_object.successfulPairs(spells, potions, 7)
		self.assertEqual(expected, actual)

  
	def test_2(self):
		spells = [15, 8, 19]
		potions = [38, 36, 23]

		test_object = Solution()

		success = 328
		expected = [3, 0, 3]
		actual = test_object.successfulPairs(spells, potions, success)
		self.assertEqual(expected, actual)