from tsp import TSPSolver

# distance matrix showing distances between cities
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

solver = TSPSolver(distance_matrix)

# solving with bfs
best_route_bfs, min_distance_bfs = solver.bfs()
print("Best route (BFS):")
solver.print_route(best_route_bfs)
print(f"Minimum distance (BFS): {min_distance_bfs}")

# solving with dfs
best_route_dfs, min_distance_dfs = solver.dfs()
print("\nBest route (DFS):")
solver.print_route(best_route_dfs)
print(f"Minimum distance (DFS): {min_distance_dfs}")

# solving with a star
best_route_astar, min_distance_astar = solver.a_star()
print("\nBest route (A*):")
solver.print_route(best_route_astar)
print(f"Minimum distance (A*): {min_distance_astar}")

# solving with greedy search
best_route_greedy, min_distance_greedy = solver.greedy_search()
print("\nBest route (Greedy Search):")
solver.print_route(best_route_greedy)
print(f"Minimum distance (Greedy Search): {min_distance_greedy}")

# solving with hill climbing
best_route_hill, min_distance_hill = solver.hill_climbing()
print("\nBest route (Hill Climbing):")
solver.print_route(best_route_hill)
print(f"Minimum distance (Hill Climbing): {min_distance_hill}")