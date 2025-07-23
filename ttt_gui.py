
import tkinter as tk
from tkinter import messagebox
import math

# Initialize the game board
board = [" " for _ in range(9)]

# Function to check if a player has won
def check_winner(player):
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combos)

# Check if the board is full
def is_full():
    return " " not in board

# Minimax algorithm for AI move decision
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
            if board[i] == " ":
                board[i] = "O"
                score = minimax(depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# Function for AI to make the best move
def ai_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    if move is not None:
        board[move] = "O"
        buttons[move].config(text="O", state="disabled")
        check_game_over()

# Function called when player clicks a button
def on_click(index):
    if board[index] == " ":
        board[index] = "X"
        buttons[index].config(text="X", state="disabled")
        if not check_game_over():
            ai_move()

# Function to check game status and show result
def check_game_over():
    if check_winner("X"):
        messagebox.showinfo("Game Over", "You win!")
        disable_all_buttons()
        return True
    elif check_winner("O"):
        messagebox.showinfo("Game Over", "AI wins!")
        disable_all_buttons()
        return True
    elif is_full():
        messagebox.showinfo("Game Over", "It's a draw!")
        disable_all_buttons()
        return True
    return False

# Disable all buttons
def disable_all_buttons():
    for button in buttons:
        button.config(state="disabled")

# Reset the game
def reset_game():
    global board
    board = [" " for _ in range(9)]
    for button in buttons:
        button.config(text=" ", state="normal")

# Create the GUI window
root = tk.Tk()
root.title("Tic Tac Toe AI")

buttons = []
for i in range(9):
    button = tk.Button(root, text=" ", font=("Arial", 20), width=5, height=2,bg="#e6f7ff",        # Light blue background
                       fg="#003366",        # Dark blue text
                       activebackground="#cceeff",  # Button color when clicked
                       activeforeground="#003366",
                       command=lambda i=i: on_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Reset button
reset_btn = tk.Button(root, text="Play Again", font=("Arial", 14),bg="#e8ffcb", fg="#73E237", command=reset_game)
reset_btn.grid(row=3, column=0, columnspan=3, sticky="we")

# Run the GUI event loop
root.mainloop()
