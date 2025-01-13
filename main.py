import tkinter as tk
from tkinter import messagebox

# Function to check if placing a queen at board[row][col] is safe
def is_safe(board, row, col):
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    return True

# Recursive function to solve N-Queens problem
def solve_n_queens(board, col):
    # Base case: If all queens are placed then return true
    if col >= len(board):
        return True

    # Try to place the queen in each row of this column col
    for i in range(len(board)):
        if is_safe(board, i, col):
            # Place the queen
            board[i][col] = 1

            # Update GUI to show current state of the board
            display_board_state(board)
            root.update_idletasks()
            root.after(500)  # Pause for 500 milliseconds

            # Recur to place rest of the queens
            if solve_n_queens(board, col + 1):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution then remove queen from board[i][col]
            board[i][col] = 0
            display_board_state(board)
            root.update_idletasks()
            root.after(500)  # Pause for 500 milliseconds

    # If the queen can't be placed in any row in this column, then return false
    return False

# Function to start solving N-Queens problem and update GUI
def start_n_queens_solver():
    try:
        n = int(entry.get())
        if n <= 0:
            messagebox.showerror("Error", "Please enter a positive integer for N.")
            return

        # Initialize the board
        board = [[0] * n for _ in range(n)]

        # Solve N-Queens problem
        if solve_n_queens(board, 0):
            messagebox.showinfo("Solution Found", f"Solution found for N = {n}.")
        else:
            messagebox.showinfo("No Solution", f"No solution found for N = {n}.")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for N.")

# Function to display the current state of the board on the GUI
def display_board_state(board):
    # Clear any previous board display
    for widget in frame.winfo_children():
        widget.destroy()

    # Draw the chessboard with queens
    for row in range(len(board)):
        for col in range(len(board)):
            color = "#EEE8AA" if (row + col) % 2 == 0 else "#8B4513"
            label_text = "♛" if board[row][col] == 1 else ""
            label_fg = "red" if board[row][col] == 1 else "black"
            label = tk.Label(frame, text=label_text, bg=color, fg=label_fg, font=("Helvetica", 32), width=3, height=1)
            label.grid(row=row, column=col, padx=2, pady=2)

# Create the main GUI window
root = tk.Tk()
root.title("N-Queens Solver")
root.configure(bg="#1C1C1C")  # Dark background for the main window

# Create a frame for the chessboard
frame = tk.Frame(root, bg="#1C1C1C")
frame.pack(pady=20)

# Create label and entry for N
label = tk.Label(root, text="Enter the value of N (N-Queens Problem):", font=("Helvetica", 14), bg="#1C1C1C", fg="#FFFFFF")
label.pack(pady=10)
entry = tk.Entry(root, font=("Helvetica", 14))
entry.pack()

# Create Solve button
solve_button = tk.Button(root, text="Solve", font=("Helvetica", 14), command=start_n_queens_solver)
solve_button.pack(pady=10)

# Run the main loop
root.mainloop()