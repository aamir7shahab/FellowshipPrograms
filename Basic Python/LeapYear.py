class LeapYear:

	# Definning constructor method
	def __init__(self,year):
		self.year = year

	# Method to print different result
	def printResult(self):
		isLeapYear = LeapYear.checkLeapYear(self.year)
		if isLeapYear == -1:
			print('Not a Valid Year')
		elif isLeapYear:
			print(f'{self.year} is a Leap Year.')
		else:
			print(f'{self.year} is a Not Leap Year.')

	# Method to check leap year or not
	def checkLeapYear(year):
		if (1000 <= year <= 9999):
			if (((year%4 == 0) and (year%100 != 0))or year%400 == 0):
				return 1
			else:
				return 0
		else: 
			return -1

if __name__ == "__main__":
	userYear = int(input("Enter year in 4 digit "))
	leapYearObject = LeapYear(userYear)
	leapYearObject.printResult()