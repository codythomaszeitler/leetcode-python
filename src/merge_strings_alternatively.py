class Solution(object):
	def mergeAlternately(self, word1, word2):
		"""
		:type word1: str
		:type word2: str
		:rtype: str
		"""
		if word1 == None:
			return word2
		if word2 == None:
			return word1

		letters = []

		i = 0
		j = 0

		while i < len(word1) or j < len(word2): 
			if i >= len(word1):
				letters.append(word2[j])
				j = j + 1
			elif j >= len(word2) :
				letters.append(word1[i])
				i = i + 1
			else:
				if (i + j) % 2 == 0:
					letters.append(word1[i])
					i = i + 1
				else:
					letters.append(word2[j])
					j = j + 1
		return ''.join(letters)

