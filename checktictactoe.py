
matrix = [[1,2,2],
          [1,2,0],
          [2,1,1]]

def row_win():
    for x in range(0,3):
        if matrix[x][0] and matrix[x][1] and matrix[x][2] != 0:
            if matrix[x][0] == matrix[x][1] == matrix[x][2]:
                print('We have a winner! The winner is player:', matrix[x][0])
                break
                
        

def column_win():
    for x in range(0,3):
        if matrix[0][x] and matrix[1][x] and matrix[2][x] != 0:
            if matrix[0][x] == matrix[1][x] == matrix[2][x]:
                print('We have a winner! The winner is player:', matrix[0][x])
                break
                
        
            
def cross_win_1():
    if matrix[0][0] and matrix[1][1] and matrix[2][2] != 0:
        if matrix[0][0] == matrix[1][1] == matrix[2][2]:
            print('We have a winner! The winner is player:', matrix[0][0])
            
        

def cross_win_2():
    if matrix[0][2] and matrix[1][1] and matrix[2][0] != 0:
        if matrix[0][2] == matrix[1][1] == matrix[2][0]:
            print('We have a winner! The winner is player:', matrix[0][2])
        
        
    

def win_check():
    row_win()
    column_win()
    cross_win_1()
    cross_win_2()
    

win_check()
    


