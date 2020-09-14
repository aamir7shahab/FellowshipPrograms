from random import randint, choice


class TicTacToe:
    # Global variables
    board = [['-', '-', '-'],
             ['-', '-', '-'],
             ['-', '-', '-']]

    availablePositions = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    winner = None
    isGameIsGoing = True
    currentPlayer = None

    # display Board fun
    @staticmethod
    def displayBoard(board):
        print(f'{board[0][0]}|{board[0][1]}|{board[0][2]}')
        print(f'{board[1][0]}|{board[1][1]}|{board[1][2]}')
        print(f'{board[2][0]}|{board[2][1]}|{board[2][2]}')
        return

    # fun to start a game
    @staticmethod
    def playGame():
        print("Lets Play Tic-Tac-Toe")
        print()
        while TicTacToe.isGameIsGoing:
            TicTacToe.handleTurn()
            TicTacToe.checkGameOver()
            TicTacToe.changePlayer()

        if TicTacToe.winner == 'X':
            print(f'Winner : {TicTacToe.winner} (Human)')
        elif TicTacToe.winner == 'O':
            print(f'Winner : {TicTacToe.winner} (Computer)')
        elif TicTacToe.winner == None:
            print('It\'s a Tie!')

    # to handle a turn
    @staticmethod
    def handleTurn():
        if TicTacToe.currentPlayer == None:
            userInput = input('Who wants to go first Human(X) or Computer(O): ')
            userInput = userInput.upper()
            if userInput == 'X' or userInput == 'O':
                TicTacToe.currentPlayer = userInput
            else:
                print('By default Human(X) goes first. ')
                TicTacToe.currentPlayer = 'X'

        if TicTacToe.currentPlayer == 'X':
            TicTacToe.humanMove()
        elif TicTacToe.currentPlayer == 'O':
            TicTacToe.cpuMove()
        TicTacToe.displayBoard(TicTacToe.board)
        print()
        return

    # check location is available or not
    @staticmethod
    def isEmpty(row, col):
        if row > len(TicTacToe.board[0]) or col > len(TicTacToe.board[0]) or row == None or col == None:
            return False
        elif TicTacToe.board[row - 1][col - 1] == '-':
            return True
        else:
            return False

    # handle human move
    @staticmethod
    def humanMove():
        position = [int(i) for i in input('Enter location in Row,Col format: ').split(',')]
        if True:
            while not TicTacToe.isEmpty(position[0], position[1]):
                print('Location not available, Try other locations: ')
                position = [int(i) for i in input('Enter location in Row,Col format: ').split(',')]
            TicTacToe.board[position[0] - 1][position[1] - 1] = TicTacToe.currentPlayer
            removeLoc = ((position[0] - 1) * len(TicTacToe.board[0])) + (position[1] - 1)
            TicTacToe.availablePositions.remove(removeLoc)
        return

    # handle CPU move
    @staticmethod
    def cpuMove():
        print('CPU (O) Turn: ')
        position = choice(TicTacToe.availablePositions)
        row = position // 3
        col = position % 3
        TicTacToe.board[row][col] = TicTacToe.currentPlayer
        TicTacToe.availablePositions.remove(position)
        return

    # change player
    @staticmethod
    def changePlayer():
        if TicTacToe.currentPlayer == 'X':
            TicTacToe.currentPlayer = 'O'
        else:
            TicTacToe.currentPlayer = 'X'
        return

    # check for game over
    @staticmethod
    def checkGameOver():
        if TicTacToe.checkForWinner():
            TicTacToe.isGameIsGoing = False
        elif TicTacToe.checkForTie():
            TicTacToe.isGameIsGoing = False
        return

    # check for winner
    @staticmethod
    def checkForWinner():
        if TicTacToe.checkRow():
            return True
        elif TicTacToe.checkCol():
            return True
        elif TicTacToe.checkDia():
            return True
        return

    # check winner in rows
    @staticmethod
    def checkRow():
        if TicTacToe.board[0][0] == TicTacToe.board[0][1] == TicTacToe.board[0][2] != '-':
            TicTacToe.winner = TicTacToe.board[0][0]
            return True
        elif TicTacToe.board[1][0] == TicTacToe.board[1][1] == TicTacToe.board[1][2] != '-':
            TicTacToe.winner = TicTacToe.board[1][0]
            return True
        elif TicTacToe.board[2][0] == TicTacToe.board[2][1] == TicTacToe.board[2][2] != '-':
            TicTacToe.winner = TicTacToe.board[2][0]
            return True
        else:
            return False

    # check winner in columns
    @staticmethod
    def checkCol():
        if TicTacToe.board[0][0] == TicTacToe.board[1][0] == TicTacToe.board[2][0] != '-':
            TicTacToe.winner = TicTacToe.board[0][0]
            return True
        elif TicTacToe.board[0][1] == TicTacToe.board[1][1] == TicTacToe.board[2][1] != '-':
            TicTacToe.winner = TicTacToe.board[0][1]
            return True
        elif TicTacToe.board[0][2] == TicTacToe.board[1][2] == TicTacToe.board[2][2] != '-':
            TicTacToe.winner = TicTacToe.board[0][2]
            return True
        else:
            return False

    # check winner in diagonal
    @staticmethod
    def checkDia():
        if TicTacToe.board[0][0] == TicTacToe.board[1][1] == TicTacToe.board[2][2] != '-':
            TicTacToe.winner = TicTacToe.board[0][0]
            return True
        elif TicTacToe.board[0][2] == TicTacToe.board[1][1] == TicTacToe.board[2][0] != '-':
            TicTacToe.winner = TicTacToe.board[0][2]
            return True
        else:
            return False

    # check for Tie
    @staticmethod
    def checkForTie():
        if '-' not in TicTacToe.board[0]:
            if '-' not in TicTacToe.board[1]:
                if '-' not in TicTacToe.board[2]:
                    TicTacToe.winner = None
                    return True


if __name__ == '__main__':
    TicTacToe.playGame()
