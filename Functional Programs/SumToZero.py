"""A program with cubic running time. Read in N integers and counts the
number of triples that sum to exactly 0."""


class SumToZero:

    @staticmethod
    def triplets(numberList):
        """
		This function takes list as input aand returns
		:param numberList:
		:return: Two variable packed as tuples. First is list of tuples (triplets) and
				Second is number of triplets present (tripletcount):
		"""
        TOTAL_SUM = 0
        triplets = []
        tripletCount = 0
        for i in range(len(numberList)):
            for j in range(i + 1, len(numberList)):
                for k in range(j + 1, len(numberList)):
                    if numberList[i] + numberList[j] + numberList[k] == TOTAL_SUM and (
                            numberList[i], numberList[j], numberList[k]) not in triplets:
                        tripletCount += 1
                        triplets.append((numberList[i], numberList[j], numberList[k]))
        return triplets, tripletCount


if __name__ == '__main__':
    listSize = int(input('Enter size of numberListay : '))
    numberList = []
    for i in range(listSize):
        askNum = int(input(f'Enter {i}th number: '))
        numberList.append(askNum)
    result = SumToZero.triplets(numberList)
    print("Triplets are:", result[1])
    print("Total triplet count: ", result[0])
