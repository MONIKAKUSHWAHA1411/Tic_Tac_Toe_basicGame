# tic_tac_toe.py

class TicTacToe:
    def __init__(self):
        """Initialize the board and set the starting player."""
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.symbols = ["💖", "💰"]
        self.current_player = 0  # Index 0: 💖, Index 1: 💰

    def display_board(self):
        """Display the board in the console."""
        for row in self.board:
            print(" | ".join(row))
            print("-" * 9)

    def make_move(self, row, col):
        """Place the current player's symbol at the given position."""
        if self.board[row][col] == " ":
            self.board[row][col] = self.symbols[self.current_player]
            if self.check_winner():
                return f"Player {self.symbols[self.current_player]} wins!"
            elif self.is_draw():
                return "It's a draw!"
            self.current_player = 1 - self.current_player  # Switch player
            return None
        return "Invalid move! Try again."

    def check_winner(self):
        """Check if the current player has won."""
        sym = self.symbols[self.current_player]

        # Check rows, columns, and diagonals
        for i in range(3):
            if all(self.board[i][j] == sym for j in range(3)):  # Rows
                return True
            if all(self.board[j][i] == sym for j in range(3)):  # Columns
                return True

        if all(self.board[i][i] == sym for i in range(3)) or \
           all(self.board[i][2 - i] == sym for i in range(3)):  # Diagonals
            return True

        return False

    def is_draw(self):
        """Check if the game is a draw (board is full)."""
        return all(self.board[i][j] != " " for i in range(3) for j in range(3))

    def reset_game(self):
        """Reset the board for a new game."""
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = 0


def main():
    """Run the game in console."""
    game = TicTacToe()

    print("Welcome to Tic-Tac-Toe with 💖 and 💰!")
    game.display_board()

    while True:
        try:
            row = int(input(f"Player {game.symbols[game.current_player]}, enter row (0-2): "))
            col = int(input(f"Player {game.symbols[game.current_player]}, enter column (0-2): "))
            result = game.make_move(row, col)
            game.display_board()
            if result:
                print(result)
                break
        except (ValueError, IndexError):
            print("Invalid input! Please enter numbers between 0 and 2.")

if __name__ == "__main__":
    main()
