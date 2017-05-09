

def take_turn(var, cycle):
    #asks current player for their marks location.
    loc = input('Player ' + var + ',' + ' Enter the position where you want to place your mark (row,column): ')
    pos = loc.split(',')
    pos = [int(x) for x in pos]
    if pos not in cycle:
        return pos
    else:
        print('Position already taken. Try again')
        pos = take_turn(var, cycle)
        return pos   

def draw_mark(pos, board, var):
    #takes player location and draws the mark on game board
    row = pos[0] 
    col = pos[1]
    board[row - 1][col - 1] = var

    return board

def main():
    #Runs tictactoe program for 9 turns
    board = [
         [0,0,0],
         [0,0,0],
         [0,0,0],
         ]
    print(board)

    cycle = []
    while len(cycle) < 9:
        if len(cycle) % 2 == 0:
            var = 'X'
            pos = take_turn(var, cycle)
            board = draw_mark(pos, board, var)
            print(board)
            cycle.append(pos)
        else:
            var = 'O'
            pos = take_turn(var, cycle)
            board = draw_mark(pos, board, var)
            print(board)
            cycle.append(pos)
    print('Game Over')

main()

            
                  
    
    


    
