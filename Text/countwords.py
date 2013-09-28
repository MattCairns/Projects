import string

def count_words():
	#Open the text file for reading
	text = open('countwords.txt', 'r')

	#Store the contents of the file in a string
	text = text.read()

	#Split the string into a list
	text = text.split(' ')

	#Return the length of the list
	return len(text)

#Print out a summary
print "There is %d words inside of the text file." % count_words()
