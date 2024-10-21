from MinMax import MinMax

class TicTacToe:
    def __init__(self):
        # create an empty board
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.minmax = MinMax()  # create an instance of MinMax

    def print_board(self):
        """print the current state of the board."""
        for i in range(3):
            print(' | '.join(self.board[i]))  # print each row
            if i < 2:  # print dashes between rows
                print('-' * 9)

    def play_game(self):
        """manage the game flow."""
        while True:
            self.print_board()
            # player 'X' turn
            self.player_move('X')
            if self.check_game_over('X'):
                break  # end game if player 'X' wins or it's a draw

            # player 'O' turn (AI)
            print("AI is making its move...")
            self.ai_move()
            if self.check_game_over('O'):
                break  # end game if player 'O' wins or it's a draw

    def player_move(self, player):
        """get player move input."""
        while True:
            move = input(f"Player {player}, enter your move (row and column, e.g., '1 1'): ")
            try:
                row, col = map(int, move.split())
                if self.board[row][col] == ' ':
                    self.board[row][col] = player  # update board with player's move
                    break
                else:
                    print("Cell is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid move. Please enter row and column as two numbers from 0 to 2.")

    def ai_move(self):
        """find the best move for AI."""
        best_value = float('-inf')
        best_move = None

        # find the best move
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'O'  # simulate AI move
                    move_value = self.minmax.minimax(self.board, 0, False)  # evaluate move
                    self.board[i][j] = ' '  # undo move
                    if move_value > best_value:
                        best_value = move_value
                        best_move = (i, j)  # update best move

        if best_move:
            self.board[best_move[0]][best_move[1]] = 'O'  # make the best move

    def check_game_over(self, player):
        """check if the game has ended."""
        if self.minmax.check_winner(self.board, player):
            self.print_board()
            print(f"Player {player} wins!")
            return True
        elif self.minmax.is_full(self.board):
            self.print_board()
            print("It's a draw!")
            return True
        return False

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
