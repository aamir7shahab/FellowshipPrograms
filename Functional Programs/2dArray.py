"""2D arrays of integers, doubles, or booleans from
standard input and printing them out to standard output."""

class D2Array:

	@staticmethod
	def userInput(rows, column, dataTypes):
		"""
		This function take the following input in a 2d list and returns list
		:param rows:
		:param column:
		:param dataTypes:
		:return: 2d List
		"""
		arr = [[0 for i in range(col)] for j in range(rows)]
		for i in range(rows):
			for j in range(column):
				if dataTypes == 'int':
					arr[i][j] = int(input(f'Enter {i*rows + j} element: '))
				elif dataTypes == 'boolean':
					arr[i][j] = bool(input(f'Enter {i*rows + j} element: '))
				else:
					arr[i][j] = str(input(f'Enter {i*rows + j} element: '))
		return print(arr)


if __name__ == '__main__':
	try:
		row = int(input('Enter the number of rows: '))
		col = int(input('Enter the number of columns: '))
	except ValueError:
		print('Error: Enter the row and columns size in integer.')
	else:
		dataType = input('Enter type of data you to enter (int,boolean,string): ')
		D2Array.userInput(row, col, dataType)