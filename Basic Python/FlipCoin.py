from random import random

class FlipCoin:

	# Definning constructor method
	def __init__(self, numberOfTimes):
		self.numberOfTimes = numberOfTimes

	# Method to carry out toss and record them
	def tossPercentage(self):
		if (self.numberOfTimes >= 0):
			tossDict = {"Head":0, "Tail":0}
			for i in range(self.numberOfTimes):
				number = random()
				if number > 0.5:
					tossDict['Tail'] += 1
				else:
					tossDict['Head'] += 1
			FlipCoin.printPercentage(tossDict)
		else:
			print("Entered number is less than zero.")

	# Method to print toss percentage
	def printPercentage(tossDict):
		totalTossCount = tossDict['Head']+tossDict['Tail']
		print(tossDict)
		print(f"Head % : {round((tossDict['Head']/totalTossCount)*100, 2)}")
		print(f"Tail % : {round((tossDict['Tail']/totalTossCount)*100, 2)}")

if __name__ == "__main__":
	numberOfTimes = int(input("Enter number of tosses: "))
	tossObject = FlipCoin(numberOfTimes)
	tossObject.tossPercentage()