def count_vowels(s):
	""" Returns the number of vowels (int) in string """
	vowels = 0
	for i in s:
		if i in 'aeiouAEIOU':
			vowels += 1

	return vowels


print count_vowels('How many vowels are in this sentance?')