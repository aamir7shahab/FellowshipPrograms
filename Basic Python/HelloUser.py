class HelloUser:
	# Defining constructor methods
	def __init__(self, userName):
		self.userName = userName

	# Method to display hello message
	def displayMessage(self):
		if (len(self.userName) > 2):
			print(f"Hello {self.userName}, How are you?")
		else:
			print("Entered name is too short!!")

if __name__ == "__main__":
	username = input("Enter your name: ")
	nameObject = HelloUser(username)
	nameObject.displayMessage()