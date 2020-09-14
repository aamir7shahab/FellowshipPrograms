class Power:

	# Definning constructor method
	def __init__(self,number):
		self.number = number

	# Method to check nmber is valid or not
	def checkValidNumber(self):
		if 0 <= self.number < 31:
			print(f"Result: {Power.powerOf2(self.number)}")
		else:
			print("Not a valid power.")

	# Method to calculate power of 2
	def powerOf2(number):
		if number == 0:
			return 1
		else:
			return Power.powerOf2(number-1)*2

if __name__ == "__main__":
	number  = int(input("Enter a Number: "))
	powerObject = Power(number)
	powerObject.checkValidNumber()