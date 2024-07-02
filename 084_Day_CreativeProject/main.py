def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True
    
    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    
    return False

def is_tie(board):
    return all([cell in ["X", "O"] for row in board for cell in row])

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while not game_over:
        try:
            row = int(input(f"Player {current_player}, enter the row (1, 2, or 3): ")) - 1
            col = int(input(f"Player {current_player}, enter the column (1, 2, or 3): ")) - 1

            if board[row][col] != " ":
                print("The cell is already taken! Try again.")
                continue

            board[row][col] = current_player
            print_board(board)

            if check_winner(board, current_player):
                print(f"Player {current_player} wins!")
                game_over = True
            elif is_tie(board):
                print("It's a tie!")
                game_over = True
            else:
                current_player = "O" if current_player == "X" else "X"

        except (ValueError, IndexError):
            print("Invalid input! Please enter a number between 1 and 3 for both row and column.")

if __name__ == "__main__":
    tic_tac_toe()
