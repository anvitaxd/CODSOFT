import math

# Tic-Tac-Toe board
def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def is_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def get_available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']

# Minimax with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    if is_winner(board, 'O'):
        return 10 - depth  # AI wins
    if is_winner(board, 'X'):
        return depth - 10  # Human wins
    if is_full(board):
        return 0  # Draw

    if is_maximizing:
        max_eval = -math.inf
        for move in get_available_moves(board):
            r, c = move
            board[r][c] = 'O'
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[r][c] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in get_available_moves(board):
            r, c = move
            board[r][c] = 'X'
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[r][c] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def best_move(board):
    best_val = -math.inf
    move = None
    for r, c in get_available_moves(board):
        board[r][c] = 'O'
        move_val = minimax(board, 0, False, -math.inf, math.inf)
        board[r][c] = ' '
        if move_val > best_val:
            best_val = move_val
            move = (r, c)
    return move

# Game loop
def play_game():
    board = create_board()
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Human move
        try:
            human_move = input("Enter your move (row and column, e.g., 1 2): ")
            r, c = map(int, human_move.split())
            if board[r][c] != ' ':
                print("Invalid move! Try again.")
                continue
            board[r][c] = 'X'
        except (ValueError, IndexError):
            print("Invalid input! Please enter row and column numbers between 0 and 2.")
            continue

        print("Your move:")
        print_board(board)

        if is_winner(board, 'X'):
            print("Congratulations! You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # AI move
        print("AI is making a move...")
        ai_move = best_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = 'O'
            print("AI's move:")
            print_board(board)

        if is_winner(board, 'O'):
            print("AI wins! Better luck next time!")
            break
        if is_full(board):
            print("It's a draw!")
            break

# Run the game
if __name__ == "__main__":
    play_game()
