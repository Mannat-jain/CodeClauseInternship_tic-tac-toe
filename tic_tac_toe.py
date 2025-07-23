import math

# Initialize the board with empty cells
board = [" " for _ in range(9)]

# Function to print the board in a 3x3 grid
def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")

# Check if a move is valid (i.e., space is empty)
def valid_move(index):
    return board[index] == " "

# Check if the board is full
def is_full():
    return " " not in board

# Check for a winner
def check_winner(player):
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in win_combos:
        if all(board[i] == player for i in combo):
            return True
    return False

# Minimax algorithm to choose the best move
def minimax(depth, is_maximizing):
    if check_winner("O"):
        return 1
    elif check_winner("X"):
        return -1
    elif is_full():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if valid_move(i):
                board[i] = "O"
                score = minimax(depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if valid_move(i):
                board[i] = "X"
                score = minimax(depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# Find the best move for the AI (O)
def best_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if valid_move(i):
            board[i] = "O"
            score = minimax(0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

# Main game loop
def play_game():
    print("Welcome to Tic Tac Toe! You are X. AI is O.")
    print_board()

    while True:
        # Human turn
        move = int(input("Enter your move (0-8): "))
        if valid_move(move):
            board[move] = "X"
        else:
            print("Invalid move. Try again.")
            continue

        print_board()

        if check_winner("X"):
            print("You win!")
            break
        elif is_full():
            print("It's a draw!")
            break

        # AI turn
        print("AI is making a move...")
        best_move()
        print_board()

        if check_winner("O"):
            print("AI wins!")
            break
        elif is_full():
            print("It's a draw!")
            break

# Run the game
if __name__ == "__main__":
    play_game()
