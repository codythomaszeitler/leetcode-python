import math

class Solution(object):
	def minEatingSpeed(self, piles, h):
		"""
		:type piles: List[int]
		:type h: int
		:rtype: int
		"""
		low = 1
		high = max(piles)

		result = high
		while high >= low:

			m = ((high - low) // 2) + low
			num_hours = self.try_eat_bananas(piles, m)

			if num_hours <= h:
				result = min(result, m)
				high = m - 1
			else:
				low = m + 1
		return result

			
	def try_eat_bananas(self, piles, k):
		result = 0
		for i in range(len(piles)):
			result += math.ceil(piles[i] / k)
		return result