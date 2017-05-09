'''Tic Tac Toe Game'''

def top_board(var1,var2, var3):
    #Draws the top part of board
    print('    |' + '    |' + '    ')
    print(' '+ str(var1) +'  |'+ ' ' + str(var2) + '  | ' + str(var3))
    print(' ------------ ')

def mid_board(var4, var5, var6):
    #Draws the middle part of board
    print('    |' + '    |' + '    ')
    print(' '+ str(var4) +'  |'+ ' ' + str(var5) + '  | ' + str(var6))
    print(' ------------ ')

def bot_board(var7, var8, var9):
    #Draws the bottom part of board
    print('    |' + '    |' + '    ')
    print(' '+ str(var7) +'  |'+ ' ' + str(var8) + '  | ' + str(var9))
    
def full_board(var1,var2,var3,var4,var5,var6,var7,var8,var9):
    #Puts entire board together 
    top_board(var1, var2, var3)
    mid_board(var4, var5, var6)
    bot_board(var7, var8, var9)
   

def take_turn(var, cycle):
    #Asks current player for their marks location.
    loc = input('Player ' + var + ',' + ' Enter the position where you want to place your mark (row,column): ')
    pos = loc.split(',')
    pos = [int(x) for x in pos]
    if 0 < pos[0] < 4 and 0 < pos[1] < 4:
        if pos not in cycle:
            return pos
        else:
            print('Position already taken. Try again')
            pos = take_turn(var, cycle)
            return pos
    else:
        print('Enter a valid row and col number.')
        pos = take_turn(var, cycle)
        return pos

def draw_mark(pos, matrix, var):
    #Takes player location and draws the mark on matrix
    row = pos[0] 
    col = pos[1]
    matrix[row - 1][col - 1] = var

    return matrix

def update_board(matrix):
    #Takes the matrix and creates an updated game board
    var1 = matrix[0][0]
    var2 = matrix[0][1]
    var3 = matrix[0][2]
    var4 = matrix[1][0]
    var5 = matrix[1][1]
    var6 = matrix[1][2]
    var7 = matrix[2][0]
    var8 = matrix[2][1]
    var9 = matrix[2][2]

    full_board(var1,var2,var3,var4,var5,var6,var7,var8,var9)
    


def row_win(matrix):
    #Checks if there is a win by row.
    for x in range(0,3):
        if matrix[x][0] and matrix[x][1] and matrix[x][2] != ' ':
            if matrix[x][0] == matrix[x][1] == matrix[x][2]:
                print('We have a winner! The winner is player:', matrix[x][0])
                return False
    

def column_win(matrix):
    #Checks if there is a win by column.
    for x in range(0,3):
        if matrix[0][x] and matrix[1][x] and matrix[2][x] != ' ':
            if matrix[0][x] == matrix[1][x] == matrix[2][x]:
                print('We have a winner! The winner is player:', matrix[0][x])
                return False
            
            
def cross_win_1(matrix):
    #Checks if there is win from left to right diagonally.
    if matrix[0][0] and matrix[1][1] and matrix[2][2] != ' ':
        if matrix[0][0] == matrix[1][1] == matrix[2][2]:
            print('We have a winner! The winner is player:', matrix[0][0])
            return False
        
def cross_win_2(matrix):
    #Checks if there is a win from right to left diagonally.
    if matrix[0][2] and matrix[1][1] and matrix[2][0] != ' ':
        if matrix[0][2] == matrix[1][1] == matrix[2][0]:
            print('We have a winner! The winner is player:', matrix[0][2])
            return False    

            
def win_check(matrix):
    #Checks for a win.
    game = True
    a = row_win(matrix)
    b = column_win(matrix)
    c = cross_win_1(matrix)
    d = cross_win_2(matrix)
    if a == False or b == False or c == False or d == False:
        game = False

    return game

def play_again():
    
    while True:
        y_n = input('Play Again? (y/n) ')
        if y_n == 'y':
            main()
        elif y_n == 'n':
            print('Goodbye')
            break
        else:
            print('Sorry, I did not catch that.')
        
def main():
    #Runs tictactoe program
    full_board(var1=' ',var2=' ',var3=' ',var4=' ',var5=' ',var6=' ',var7=' ',var8=' ',var9=' ')
    matrix = [
         [' ',' ',' '],
         [' ',' ',' '],
         [' ',' ',' '],
         ]
    
    cycle = []
    game = True
    while len(cycle) < 9 and game == True:
        
        if len(cycle) % 2 == 0:
            var = 'X'
            pos = take_turn(var, cycle)
            matrix = draw_mark(pos, matrix, var)
            cycle.append(pos)
            update_board(matrix)
            
                    
        
        else:
            var = 'O'
            pos = take_turn(var, cycle)
            matrix = draw_mark(pos, matrix, var)
            cycle.append(pos)
            update_board(matrix)
            
        game = win_check(matrix)    
        
    print('Game Over')
    play_again()

main()
         
                  

