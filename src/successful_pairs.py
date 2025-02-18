class Solution(object):
	def successfulPairs(self, spells, potions, success):
		"""
		:type spells: List[int]
		:type potions: List[int]
		:type success: int
		:rtype: List[int]
		"""
		potions.sort()
		result = [0 for _ in range(len(spells))]
		for i in range(len(spells)):
			index = self.find_starting_index(spells[i], potions, success)
			if index != -1:
				result[i] = len(potions) - index
		return result
	
	def find_starting_index(self, spell, potions, success):
		l = 0
		r = len(potions)

		while r > l:
			m = ((r - l) // 2) + l
			result = spell * potions[m]
			if result >= success:
				if m == 0:
					return m
				if spell * potions[m - 1] < success:
					return m	
				r = m
			else:
				l = m + 1
		return -1