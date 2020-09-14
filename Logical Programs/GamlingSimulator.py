from random import choice


class GamlingSimulator:
    resultArr = []
    resultDic = {'Won': 0, 'Lost': 0}

    @staticmethod
    def gamble(stake, goal, trail):
        if stake == 0 or stake == goal or trail == 0:
            return GamlingSimulator.resultArr, GamlingSimulator.resultDic, stake
        else:
            oneBetResult = choice([-1, 1])
            if oneBetResult == -1:
                GamlingSimulator.resultArr.append((0, 1))
                GamlingSimulator.resultDic['Won'] += 1
                return GamlingSimulator.gamble(stake - oneBetResult, goal, trail - 1)
            else:
                GamlingSimulator.resultArr.append((1, 0))
                GamlingSimulator.resultDic['Lost'] += 1
                return GamlingSimulator.gamble(stake - oneBetResult, goal, trail - 1)

    @staticmethod
    def printResult(arr, dict1):
        print(f' Won  :  Lost ')
        for i in arr:
            print(f' {i[0]:^3}  : {i[1]:^5} ')
        print('*' * 14)
        for i in dict1.keys():
            print(f'{i:^5} :{dict1[i]:^7}')


if __name__ == '__main__':
    stake = int(input('Enter starting stake : '))
    goal = int(input('Enter the goal : '))
    trails = int(input('Enter number of times you want to gamble : '))
    arr, result, balance = GamlingSimulator.gamble(stake, goal, trails)
    GamlingSimulator.printResult(arr, result)
    print(f'Grand Total : {balance}')
