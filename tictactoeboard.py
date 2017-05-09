'''Creates a square shaped game board based on user's preference.'''

def top_layer(size):
    #Makes the top portion of the board.
    print(' --- ' * size)
    print('|    ' * (size+1))

def bottom_layer(size):
    #Makes the bottom potion of the board.
    print(' --- ' * size)

def main():
    #Runs program
    size = int(input('Enter the size of board: '))
    x = size

    while x > 0:
        top_layer(size)
        x -= 1

    bottom_layer(size)

main()



    
    
