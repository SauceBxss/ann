from AlphaBetaPruning import minimax_with_alpha_beta
import math

if __name__ == "__main__":
    # set up root node, tree depth, and alpha-beta values
    root_node = 'A'
    max_depth = 3
    initial_alpha = -math.inf
    initial_beta = math.inf

    # run minimax with alpha-beta pruning from the root node
    optimal_value = minimax_with_alpha_beta(root_node, max_depth, initial_alpha, initial_beta, False)

    # print the optimal value
    print(f"The optimal value for the root node is: {optimal_value}")
