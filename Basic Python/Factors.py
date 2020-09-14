class Factor:
	
	# Definning constructor method
	def __init__(self,number):
		self.number = number

	# Method to print element of the list
	def printNumberOfList(numberList):
		print("Factors are :", end=' ')
		for i in numberList:
			print(i, end=' ')
		print()

	# Method to find prime or not
	def isPrime(number):
		flag = 1
		for i in range(2, (number//2)+1):
			if number%i == 0:
				flag = 0
				break
		if flag:
			return 1
		else:
			return 0

	# Method to find prime factor
	def findFactors(self):
		factors = []
		i = 2
		while self.number != 1:
			if Factor.isPrime(i) and self.number%i == 0:
				factors.append(i)
				self.number = (self.number)/i
				i = 2
			else:
				i += 1
		Factor.printNumberOfList(factors)

if __name__ == "__main__":
	number = int(input('Enter a number: '))
	factorObject = Factor(number)
	factorObject.findFactors()