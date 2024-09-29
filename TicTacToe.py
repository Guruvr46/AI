import math

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Check if there are any moves left on the board
def is_moves_left(board):
    for row in board:
        if "_" in row:
            return True
    return False

# Evaluate the board: +10 for win, -10 for loss, 0 for draw
def evaluate(board):
    # Check for rows for victory
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != "_":
            return 10 if board[row][0] == "X" else -10
    
    # Check for columns for victory
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "_":
            return 10 if board[0][col] == "X" else -10
    
    # Check for diagonals for victory
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "_":
        return 10 if board[0][0] == "X" else -10
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "_":
        return 10 if board[0][2] == "X" else -10
    
    # No one has won yet
    return 0

# Minimax algorithm to find the optimal move
def minimax(board, depth, is_max):
    score = evaluate(board)

    # If the maximizer or minimizer has won, return the evaluated score
    if score == 10:
        return score - depth  # Subtract depth to prioritize quicker wins
    if score == -10:
        return score + depth  # Add depth to prioritize delaying losses

    # If no moves are left and no one has won, it's a tie
    if not is_moves_left(board):
        return 0

    # Maximizer's move
    if is_max:
        best = -math.inf

        for i in range(3):
            for j in range(3):
                # Check if the cell is empty
                if board[i][j] == "_":
                    board[i][j] = "X"
                    best = max(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = "_"  # Undo the move
        return best

    # Minimizer's move
    else:
        best = math.inf

        for i in range(3):
            for j in range(3):
                # Check if the cell is empty
                if board[i][j] == "_":
                    board[i][j] = "O"
                    best = min(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = "_"  # Undo the move
        return best

# Function to find the best move for the AI
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                board[i][j] = "X"
                move_val = minimax(board, 0, False)
                board[i][j] = "_"  # Undo the move

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# Function to check for a winner
def check_winner(board):
    score = evaluate(board)
    if score == 10:
        return "AI (X) wins!"
    elif score == -10:
        return "Player (O) wins!"
    elif not is_moves_left(board):
        return "It's a tie!"
    return None

# Main function to play the game
def play_tic_tac_toe():
    board = [
        ["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"]
    ]

    print("Welcome to Tic-Tac-Toe!")
    print("You are 'O' and AI is 'X'.")
    
    print_board(board)

    while is_moves_left(board):
        # Player's move
        row, col = map(int, input("Enter your move (row and column): ").split())
        
        if board[row][col] == "_":
            board[row][col] = "O"
        else:
            print("Invalid move! Try again.")
            continue

        print_board(board)

        # Check if player won
        winner = check_winner(board)
        if winner:
            print(winner)
            break

        # AI's move
        print("AI is making a move...")
        best_move = find_best_move(board)
        board[best_move[0]][best_move[1]] = "X"
        print_board(board)

        # Check if AI won
        winner = check_winner(board)
        if winner:
            print(winner)
            break

if __name__ == "__main__":
    play_tic_tac_toe()
