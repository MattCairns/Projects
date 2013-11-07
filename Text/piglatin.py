def pig_latin(s):
	s = s.lower()
	s = s.split()
	pig_s = []
	for i in s:
		if i[0] in 'aeiouAEIOU':
			i += 'way'
			pig_s.append(i)

		else:
			i = i[1:] + i[0] + 'ay'
			pig_s.append(i)

	return ' '.join(pig_s)

print pig_latin(raw_input('Enter something: '))
