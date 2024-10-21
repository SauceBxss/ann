"""
definitions:
    minimax algorithm:
        the minimax algorithm helps decide the best move in two-player games where one player's gain is the other's loss. it looks at all possible moves to find the best one for both players. the players are:
            * maximizer: a player trying to maximize the score (usually the main player).
            * minimizer: a player trying to minimize the score (usually the opponent).
        the minimax algorithm assumes both players play optimally and selects moves based on the idea that the maximizer tries to maximize the score and the minimizer tries to minimize it.
        
    alpha-beta pruning:
        alpha-beta pruning is an optimization technique for the minimax algorithm that reduces the number of nodes evaluated in the game tree. it prunes branches of the tree that are not necessary to evaluate, making the algorithm more efficient without affecting the result.

        alpha: the best value that the maximizer can guarantee.
        beta: the best value that the minimizer can guarantee.
        pruning works by:
            * updating the alpha value when the maximizer finds a better move.
            * updating the beta value when the minimizer finds a worse move.
            * pruning branches when a move is found that makes further exploration unnecessary (i.e., when alpha >= beta).
"""

# simulated game tree with node values (example game states)
# the structure maps each node to its child nodes or final evaluation if terminal
# """
#         A
#        / \
#       B   C
#      / \ / \
#    D  E F  G
#   -1  3 5  0

#     A is the root node.
#     B and C are child nodes of A.
#     D, E, F, and G are terminal nodes with corresponding evaluation values (-1, 3, 5, 0).
# """
game_tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': -1,  # terminal node
    'E': 3,   # terminal node
    'F': 5,   # terminal node
    'G': 0    # terminal node
}

# function to get children of a node (non-terminal nodes have children, terminal nodes don't)
"""
    returns the child nodes of the current node. if the node has no children (terminal node), it returns an empty list.
"""
def get_children(node):
    return game_tree.get(node, [])

# function to determine if a node is terminal (i.e., no children)
"""
    checks if a node is terminal (has no children) by confirming if its value is an integer rather than a list of child nodes.
"""
def is_terminal_node(node):
    return not isinstance(game_tree[node], list)

# function to evaluate a terminal node by returning its heuristic value
def evaluate(node):
    return game_tree[node]  # terminal nodes are mapped to their evaluation scores

# minimax algorithm with alpha-beta pruning
"""
    implements the minimax algorithm with alpha-beta pruning. the algorithm searches the game tree, alternating between maximizing and minimizing player decisions, and prunes subtrees where further exploration is unnecessary.
"""
def minimax_with_alpha_beta(node, depth, alpha, beta, maximizingPlayer):
    """
    implements the minimax algorithm with alpha-beta pruning.

    parameters:
    node (str): the current node in the game tree.
    depth (int): the depth of the game tree to explore.
    alpha (float): the best value that the maximizer can guarantee so far.
    beta (float): the best value that the minimizer can guarantee so far.
    maximizingPlayer (bool): true if the current player is the maximizer, false if the minimizer.

    returns:
    int: the optimal value for the current node.
    """
    # base case: return the evaluation of terminal node or reach the depth limit
    if depth == 0 or is_terminal_node(node):
        return evaluate(node)  # returns the heuristic value of the node

    if maximizingPlayer:
        max_eval = float('-inf')  # initialize the worst case for maximizer
        for child in get_children(node):  # explore each child of the current node
            eval = minimax_with_alpha_beta(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)  # maximizer chooses the maximum value
            alpha = max(alpha, eval)  # update alpha (best guarantee for maximizer)
            if beta <= alpha:
                print(f"pruning at node {node} with alpha={alpha}, beta={beta}")
                break  # beta cutoff (prune the branch)
        return max_eval
    else:
        min_eval = float('inf')  # initialize the worst case for minimizer
        for child in get_children(node):  # explore each child of the current node
            eval = minimax_with_alpha_beta(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)  # minimizer chooses the minimum value
            beta = min(beta, eval)  # update beta (best guarantee for minimizer)
            if beta <= alpha:
                print(f"pruning at node {node} with alpha={alpha}, beta={beta}")
                break  # alpha cutoff (prune the branch)
        return min_eval
