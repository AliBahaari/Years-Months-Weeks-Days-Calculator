"""
A simple calculator for years, months, weeks and days.
"""

number = input('Enter a Number for Calculation: ')

if number.isnumeric():

	number = int(number)


	# Begins Years
	if number >= 365:

		years = number // 365
		yearsRemainder = number % 365

		months = yearsRemainder // 30
		monthsRemainder = yearsRemainder % 30

		weeks = monthsRemainder // 7
		weeksRemainder = monthsRemainder % 7

		days = weeksRemainder // 1

		print('Years: ' + str(years) + ', Months: ' + str(months) + ', Week: ' + str(weeks) + ', Days: ' + str(days))


	# Begins Months
	elif number < 365 and number >= 30:

		months = number // 30
		monthsRemainder = number % 30

		weeks = monthsRemainder // 7
		weeksRemainder = monthsRemainder % 7

		days = weeksRemainder // 1

		print('Months: ' + str(months) + ', Week: ' + str(weeks) + ', Days: ' + str(days))


	# Begins Weeks
	elif number < 30 and number >= 7:

		weeks = number // 7
		weeksRemainder = number % 7

		days = weeksRemainder // 1

		print('Week: ' + str(weeks) + ', Days: ' + str(days))


	# Begins Days
	elif number < 7:

		print('Days: ' + str(number))

else:
	print('Enter a Number!')
