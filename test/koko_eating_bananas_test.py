import unittest
from src.koko_eating_bananas import Solution

class KokoEatingBananasTest(unittest.TestCase):

	def test_1(self):
		piles = [3, 6, 7, 11]
		h = 8
		test_object = Solution()

		k = test_object.minEatingSpeed(piles, h)

		self.assertEqual(4, k)
	
	def test_2(self):
		piles = [30,11,23,4,20]
		h = 5
		test_object = Solution()
  
		k = test_object.minEatingSpeed(piles, h)
		self.assertEqual(30, k)

	def test_3(self):
		piles = [30,11,23,4,20]
		h = 6
		test_object = Solution()
		k = test_object.minEatingSpeed(piles, h)
		self.assertEqual(23, k)