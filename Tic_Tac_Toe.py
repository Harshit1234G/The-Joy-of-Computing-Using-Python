board = [[' ' for _ in range(3)] for _ in range(3)]

def draw_board():
    '''
    Draws the board of the Tic Tac Toe
    '''
    print(' ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2])
    print('-----------')
    print(' ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2])
    print('-----------')
    print(' ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2])

def get_move(player):
    '''
    Takes the move from the user according to the player passed to the function
    '''
    while True:
        move = input(f'{player}, enter your move (row column): ')
        try:
            row, col = map(int, move.split())
            if row in [0, 1, 2] and col in [0, 1, 2] and board[row][col] == ' ': # --> checking if the slot is empty and in range of board
                board[row][col] = player
                break
            else:
                print('Invalid move, try again.')
        except ValueError:
            print('Invalid input, try again.')

def has_won(player):
    '''
    Retruns true if any player wons
    '''
    # check rows
    for row in range(3):
        if all(cell == player for cell in board[row]):
            return True
    # check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def check_draw():
    '''
    Checks if the game is draw
    '''
    d = 0
    for row in range(3):
        if all(board[row][col] != ' ' for col in range(3)):
            d += 1
    
    if d == 3:
        return True
    

if __name__ == "__main__":

    draw_board()

    while True:
        get_move('X')
        draw_board()
        
        if check_draw() and (has_won('X') and has_won('O')) is False:
            print("The match is draw!")
            break
        
        if has_won('X'):
            print('X has won!')
            break

        get_move('O')
        draw_board()

        if has_won('O'):
            print('O has won!')
            break
