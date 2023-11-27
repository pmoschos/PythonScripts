import tkinter as tk
from tkinter import messagebox

def check_win():
    # Check for winning conditions
    for i in range(3):
        # Check rows and columns
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None

def check_draw():
    return all(all(row) for row in board)

def on_button_click(r, c):
    if board[r][c] == "" and not check_win():
        board[r][c] = "X" if turn[0] else "O"
        buttons[r][c].config(text=board[r][c])
        if check_win():
            messagebox.showinfo("Tic Tac Toe", f"{'X' if turn[0] else 'O'} wins!")
            reset_board()
        elif check_draw():
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            reset_board()
        turn[0] = not turn[0]

def reset_board():
    for r in range(3):
        for c in range(3):
            buttons[r][c].config(text="")
            board[r][c] = ""
    turn[0] = True

# Tkinter setup
window = tk.Tk()
window.title("Tic Tac Toe")

# Game state variables
turn = [True]  # List used to make it mutable in nested function
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

# Create buttons
for r in range(3):
    for c in range(3):
        button = tk.Button(window, text="", font=('normal', 40), width=5, height=2,
                           command=lambda r=r, c=c: on_button_click(r, c))
        button.grid(row=r, column=c)
        buttons[r][c] = button

# Reset button
reset_button = tk.Button(window, text='Reset', font=('normal', 15), command=reset_board)
reset_button.grid(row=3, column=0, columnspan=3)

# Run the main loop
window.mainloop()
