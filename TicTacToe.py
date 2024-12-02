import random

# Initialize the board
def init_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def player_move(board):
    while True:
        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
            if board[row][col] == " ":
                board[row][col] = "X"
                break  # Valid move, exit loop
            else:
                print("Invalid move. Try again.")
        except (ValueError, IndexError):
            print("Please enter valid row and column numbers (0, 1, 2).")

def computer_move(board):
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = "O"

def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]
    ]
    return [player, player, player] in win_conditions

def check_tie(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = init_board()

    while True:
        print_board(board)
        
        # Player move
        player_move(board)
        if check_winner(board, "X"):
            print_board(board)
            print("Player wins!")
            break
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break
        
        # Computer move
        computer_move(board)
        if check_winner(board, "O"):
            print_board(board)
            print("Computer wins!")
            break
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

    # Ask if the player wants to play again
    restart = input("Do you want to play again? (y/n): ").strip().lower()
    if restart == 'y':
        tic_tac_toe()  # Restart the game
    else:
        print("Thanks for playing!")

# Run the game
tic_tac_toe()
