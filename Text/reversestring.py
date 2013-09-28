def reverse_string(text):
	newText = ''
	for letter in reversed(xrange(len(text))):
		newText = newText + text[letter]
	return newText


print reverse_string('I will be reversed!!')