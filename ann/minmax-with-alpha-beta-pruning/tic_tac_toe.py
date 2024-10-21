import math

# constants
PLAYER_X = 'X'  # ai player
PLAYER_O = 'O'  # human player
EMPTY = '_'


class TicTacToe:
    def __init__(self):
        self.board = [
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]
        ]

    def print_board(self):
        """print the tic-tac-toe board."""
        for row in self.board:
            print(' '.join(row))
        print()

    def is_full(self):
        """check if the board is full."""
        for row in self.board:
            if EMPTY in row:
                return False
        return True

    def check_winner(self):
        """check if there is a winner."""
        # check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != EMPTY:
                return row[0]

        # check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != EMPTY:
                return self.board[0][col]

        # check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != EMPTY:
            return self.board[0][0]

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != EMPTY:
            return self.board[0][2]

        return None

    def is_terminal(self):
        """check if the game has ended (either win or draw)."""
        return self.check_winner() is not None or self.is_full()

    def get_available_moves(self):
        """get a list of available moves."""
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == EMPTY:
                    moves.append((i, j))
        return moves

    def make_move(self, row, col, player):
        """make a move on the board."""
        self.board[row][col] = player

    def undo_move(self, row, col):
        """undo a move on the board."""
        self.board[row][col] = EMPTY

    def minimax(self, depth, is_maximizing, alpha, beta):
        """minimax algorithm with alpha-beta pruning."""
        winner = self.check_winner()
        if winner == PLAYER_X:
            return 10 - depth  # ai wins
        elif winner == PLAYER_O:
            return depth - 10  # human wins
        elif self.is_full():
            return 0  # draw

        if is_maximizing:
            max_eval = -math.inf
            for move in self.get_available_moves():
                self.make_move(move[0], move[1], PLAYER_X)
                eval = self.minimax(depth + 1, False, alpha, beta)
                self.undo_move(move[0], move[1])
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = math.inf
            for move in self.get_available_moves():
                self.make_move(move[0], move[1], PLAYER_O)
                eval = self.minimax(depth + 1, True, alpha, beta)
                self.undo_move(move[0], move[1])
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def best_move(self):
        """find the best move for ai using minimax with alpha-beta pruning."""
        best_val = -math.inf
        best_move = None

        for move in self.get_available_moves():
            self.make_move(move[0], move[1], PLAYER_X)
            move_val = self.minimax(0, False, -math.inf, math.inf)
            self.undo_move(move[0], move[1])

            if move_val > best_val:
                best_val = move_val
                best_move = move

        return best_move

    def play_game(self):
        """main function to play the game."""
        print("Welcome to Tic-Tac-Toe!")
        self.print_board()

        while not self.is_terminal():
            # human move
            row, col = map(int, input("Enter your move (row and column): ").split())
            if self.board[row][col] == EMPTY:
                self.make_move(row, col, PLAYER_O)
                self.print_board()

                if self.is_terminal():
                    break

                # ai move
                print("AI is making a move...")
                move = self.best_move()
                if move:
                    self.make_move(move[0], move[1], PLAYER_X)
                    self.print_board()
            else:
                print("Invalid move, try again.")

        winner = self.check_winner()
        if winner == PLAYER_X:
            print("AI wins!")
        elif winner == PLAYER_O:
            print("You win!")
        else:
            print("It's a draw!")


if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
