"""
    minimax algorithm:
        this algorithm helps decide the best move in two-player games where one player's gain is the other's loss. it looks at all possible moves to find the best one for both players. the players are:
            * maximizer: the player trying to get the highest score (usually the main player).
            * minimizer: the player trying to get the lowest score (usually the opponent).
        the algorithm assumes both players play their best and chooses moves based on the maximizer's goal to increase the score and the minimizer's goal to decrease it.
"""
class MinMax:
    def minimax(self, board, depth, is_maximizing):
        """
        minimax algorithm to find the best move for the maximizing player.

        :param board: current state of the tic-tac-toe board.
        :param depth: how many moves ahead to consider.
        :param is_maximizing: true if it's the maximizing player's turn (true for 'X', false for 'O').
        :return: best value for the maximizing player based on the board's evaluation.
        """

        # check if the game has ended and return score.
        if self.check_winner(board, 'X'):
            return 10 - depth  # 'X' wins
        elif self.check_winner(board, 'O'):
            return depth - 10  # 'O' wins
        elif self.is_full(board):
            return 0  # draw

        if is_maximizing:
            best_value = float('-inf')  # lowest possible value
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = 'X'  # simulate 'X' move
                        value = self.minimax(board, depth + 1, False)  # minimize for 'O'
                        board[i][j] = ' '  # undo move
                        best_value = max(best_value, value)  # get the maximum score
            return best_value
        else:
            best_value = float('inf')  # highest possible value
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = 'O'  # simulate 'O' move
                        value = self.minimax(board, depth + 1, True)  # maximize for 'X'
                        board[i][j] = ' '  # undo move
                        best_value = min(best_value, value)  # get the minimum score
            return best_value

    def check_winner(self, board, player):
        """
        check if the player has won.

        :param board: current state of the tic-tac-toe board.
        :param player: the player to check for ('X' or 'O').
        :return: true if the player has won, false otherwise.
        """
        # check rows, columns, and diagonals for a win
        for i in range(3):
            if all([cell == player for cell in board[i]]):  # check rows
                return True
            if all([board[j][i] == player for j in range(3)]):  # check columns
                return True
        if all([board[i][i] == player for i in range(3)]):  # check diagonal
            return True
        if all([board[i][2 - i] == player for i in range(3)]):  # check anti-diagonal
            return True
        return False

    def is_full(self, board):
        """
        check if the board is full.

        :param board: current state of the tic-tac-toe board.
        :return: true if the board is full, false otherwise.
        """
        return all(cell != ' ' for row in board for cell in row)
