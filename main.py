import os
clear_screen = lambda: os.system('clear')

playerXValue = 'X'
playerZeroValue = '0'
playerXWinValue = playerXValue*3
playerZeroWinValue = playerZeroValue*3
emptyFieldPlace = ' '

class GameState:
  def __init__(self):
    self.isSomeOneWin = False
    self.gameMessage = ''
    self.isTKo = False
    self.isXPlayerStep = True
    self.lastStep = None

playFieldColors = [
    ['\033[93m', '\033[93m', '\033[93m', '\033[93m'],
    ['\033[93m', '\33[37m', '\33[37m', '\33[37m'],
    ['\033[93m', '\33[37m', '\33[37m', '\33[37m'],
    ['\033[93m', '\33[37m', '\33[37m', '\33[37m'],
]
WINCOLOR = '\033[92m'


playField = [
    [' ', '1', '2', '3'],
    ['1', emptyFieldPlace, emptyFieldPlace, emptyFieldPlace],
    ['2', emptyFieldPlace, emptyFieldPlace, emptyFieldPlace],
    ['3', emptyFieldPlace, emptyFieldPlace, emptyFieldPlace],
]

def printField(field):
    print('\n'.join([' '.join([f'{playFieldColors[j][i]}{cell}' for i,cell in enumerate(row)]) for j,row in enumerate(field)]))

def checkGameField(gs):
    for i in [x+1 for x in range(3)]:
        row_sum = ""
        for j in [x+1 for x in range(3)]:
            row_sum += playField[i][j]
        if row_sum == playerXWinValue:
            gs.isSomeOneWin = True
            gs.gameMessage = 'Player X Win !!!'
        elif row_sum == playerZeroWinValue:
            gs.isSomeOneWin = True
            gs.gameMessage = 'Player Zero Win !!!'

        if gs.isSomeOneWin:
            playFieldColors[i][1] = WINCOLOR
            playFieldColors[i][2] = WINCOLOR
            playFieldColors[i][3] = WINCOLOR
            return gs

    for i in [x+1 for x in range(3)]:
        col_sum = ""
        for j in [x+1 for x in range(3)]:
            col_sum += playField[j][i]
            if col_sum == playerXWinValue:
                gs.isSomeOneWin = True
                gs.gameMessage = 'Player X Win !!!'
            elif col_sum == playerZeroWinValue:
                gs.isSomeOneWin = True
                gs.gameMessage = 'Player Zero Win !!!'

            if gs.isSomeOneWin:
                playFieldColors[1][i] = WINCOLOR
                playFieldColors[2][i] = WINCOLOR
                playFieldColors[3][i] = WINCOLOR
                return gs

    if (playField[1][1] + playField[2][2] + playField[3][3]) == playerXWinValue:
        playFieldColors[1][1] = WINCOLOR
        playFieldColors[2][2] = WINCOLOR
        playFieldColors[3][3] = WINCOLOR
        gs.isSomeOneWin = True
        gs.gameMessage = 'Player X Win !!!'
        return gs
    if (playField[1][1] + playField[2][2] + playField[3][3]) == playerZeroWinValue:
        playFieldColors[1][1] = WINCOLOR
        playFieldColors[2][2] = WINCOLOR
        playFieldColors[3][3] = WINCOLOR
        gs.isSomeOneWin = True
        gs.gameMessage = 'Player Zero Win !!!'
        return gs

    if (playField[3][1] + playField[2][2] + playField[1][3]) == playerXWinValue:
        playFieldColors[1][3] = WINCOLOR
        playFieldColors[2][2] = WINCOLOR
        playFieldColors[3][1] = WINCOLOR
        gs.isSomeOneWin = True
        gs.gameMessage = 'Player X Win !!!'
        return gs
    if (playField[3][1] + playField[2][2] + playField[1][3]) == playerZeroWinValue:
        playFieldColors[1][3] = WINCOLOR
        playFieldColors[2][2] = WINCOLOR
        playFieldColors[3][1] = WINCOLOR
        gs.isSomeOneWin = True
        gs.gameMessage = 'Player Zero Win !!!'
        return gs

    gs.isTKo = True
    for i in [x+1 for x in range(3)]:
        for j in [x+1 for x in range(3)]:
            if playField[i][j] == emptyFieldPlace:
                gs.isTKo = False

    if gs.isTKo:
        gs.gameMessage = 'TKO Win !!!'
    return gs

gameState = GameState()

while not (gameState.isSomeOneWin or gameState.isTKo):
    clear_screen()
    printField(playField)
    gameState = checkGameField(gameState)

    if not (gameState.isSomeOneWin or gameState.isTKo):
        entered_correct = False
        count_enter = 0
        was_except = False
        while not entered_correct:
            count_enter += 1
            if count_enter > 1:
                clear_screen()
                printField(playField)
                FAILCOLOR = '\033[91m'
                if was_except:
                    print(f'{FAILCOLOR}Please be careful !!!')
                print(f'{FAILCOLOR}Entered step not correct !!!')
            new_step = input('Player X enter your step:' if gameState.isXPlayerStep else 'Player Zero enter your step:')
            was_except = False
            playerStep = None
            try:
                playerStep = list(map(lambda el: int(el) if 0< int(el) < 4 else 0, new_step.split()))
                if playField[playerStep[1]][playerStep[0]] != emptyFieldPlace:
                    continue
                if all(playerStep):
                    entered_correct = True
                    playField[playerStep[1]][playerStep[0]] = playerXValue if gameState.isXPlayerStep else playerZeroValue
                    gameState.isXPlayerStep = not gameState.isXPlayerStep
            except:
                was_except = True

clear_screen()
printField(playField)
print('\n', f'{WINCOLOR}{gameState.gameMessage}')


