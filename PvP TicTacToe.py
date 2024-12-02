import random

# Initialize the board
def init_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def player_move(board, player):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0, 1, 2): "))
            col = int(input(f"Player {player}, enter column (0, 1, 2): "))
            if board[row][col] == " ":
                board[row][col] = player
                break  # Valid move, exit loop
            else:
                print("Invalid move. Try again.")
        except (ValueError, IndexError):
            print("Please enter valid row and column numbers (0, 1, 2).")

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

def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 1  # AI wins
    if check_winner(board, "X"):
        return -1  # Player wins
    if check_tie(board):
        return 0  # Tie

    if is_maximizing:
        best_score = -float('inf')
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = "O"
                    score = minimax(board, depth + 1, False)
                    board[r][c] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = "X"
                    score = minimax(board, depth + 1, True)
                    board[r][c] = " "
                    best_score = min(score, best_score)
        return best_score

def computer_move(board):
    best_score = -float('inf')
    best_move = None
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                board[r][c] = "O"
                score = minimax(board, 0, False)
                board[r][c] = " "
                if score > best_score:
                    best_score = score
                    best_move = (r, c)
    if best_move:
        board[best_move[0]][best_move[1]] = "O"

def tic_tac_toe():
    board = init_board()

    # Choose game mode
    mode = input("Choose game mode: 1 for Human vs. Human, 2 for Human vs. Computer: ").strip()

    while True:
        print_board(board)

        # Player X move
        player_move(board, "X")
        if check_winner(board, "X"):
            print_board(board)
            print("Player X wins!")
            break
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break
        
        if mode == "2":
            # Computer move (Player O)
            computer_move(board)
            if check_winner(board, "O"):
                print_board(board)
                print("Computer wins!")
                break
        else:
            # Player O move
            print_board(board)
            player_move(board, "O")
            if check_winner(board, "O"):
                print_board(board)
                print("Player O wins!")
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
