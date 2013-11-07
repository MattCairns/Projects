def check_card(ccn):
	"""
	Checks if a credit card number is valid or not (True/False)
	This uses the Luhn algorithm.
	@Parameters:
		ccn: The credit card number as a string.
	@Returns:
		Boolean.
	"""
	last_digit = int(ccn[-1])
	ccn = ccn[:-1]
	ccn = ccn[::-1]
	print ccn
	temp_ccn = []

	for i in range(1, len(ccn)+1):
		num = int(ccn[i-1])
		if i%2 != 0:
			num *= 2
			if num > 9:
				num -= 9
			temp_ccn.append(num)

		else:
			temp_ccn.append(num)

	return sum(temp_ccn)%10 == last_digit



print check_card('4556737586899855') #This number isn't real but is valid