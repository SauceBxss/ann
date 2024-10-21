from collections import deque

# function to check if a state has been visited
def is_visited(visited_states, state):
    return state in visited_states

# function to show the steps taken to reach the solution
def display_steps(steps):
    for i, step in enumerate(steps):
        print(f"Step {i + 1}: Jug 1 = {step[0]}L, Jug 2 = {step[1]}L")

# bfs for water jug problem
def bfs_water_jug(jug1_capacity, jug2_capacity, target_amount):
    queue = deque([(0, 0, [])])  # start with both jugs empty and no steps
    visited_states = set()       # set to keep track of visited states

    while queue:
        jug1, jug2, steps = queue.popleft()

        if jug1 == target_amount or jug2 == target_amount:
            steps.append((jug1, jug2))
            return steps

        if is_visited(visited_states, (jug1, jug2)):
            continue

        visited_states.add((jug1, jug2))

        # add all possible next states to the queue
        queue.append((jug1_capacity, jug2, steps + [(jug1, jug2)]))  # fill jug 1
        queue.append((jug1, jug2_capacity, steps + [(jug1, jug2)]))  # fill jug 2
        queue.append((0, jug2, steps + [(jug1, jug2)]))              # empty jug 1
        queue.append((jug1, 0, steps + [(jug1, jug2)]))              # empty jug 2

        # pour from jug 1 to jug 2
        transfer = min(jug1, jug2_capacity - jug2)
        queue.append((jug1 - transfer, jug2 + transfer, steps + [(jug1, jug2)]))

        # pour from jug 2 to jug 1
        transfer = min(jug2, jug1_capacity - jug1)
        queue.append((jug1 + transfer, jug2 - transfer, steps + [(jug1, jug2)]))

    return None  # if no solution is found

# dfs for water jug problem
def dfs_water_jug(jug1_capacity, jug2_capacity, target_amount):
    stack = [(0, 0, [])]  # start with both jugs empty and no steps
    visited_states = set()  # set to keep track of visited states

    while stack:
        jug1, jug2, steps = stack.pop()

        if jug1 == target_amount or jug2 == target_amount:
            steps.append((jug1, jug2))
            return steps

        if is_visited(visited_states, (jug1, jug2)):
            continue

        visited_states.add((jug1, jug2))

        # add all possible next states to the stack
        stack.append((jug1_capacity, jug2, steps + [(jug1, jug2)]))  # fill jug 1
        stack.append((jug1, jug2_capacity, steps + [(jug1, jug2)]))  # fill jug 2
        stack.append((0, jug2, steps + [(jug1, jug2)]))              # empty jug 1
        stack.append((jug1, 0, steps + [(jug1, jug2)]))              # empty jug 2

        # pour from jug 1 to jug 2
        transfer = min(jug1, jug2_capacity - jug2)
        stack.append((jug1 - transfer, jug2 + transfer, steps + [(jug1, jug2)]))

        # pour from jug 2 to jug 1
        transfer = min(jug2, jug1_capacity - jug1)
        stack.append((jug1 + transfer, jug2 - transfer, steps + [(jug1, jug2)]))

    return None  # if no solution is found

# main function to test bfs and dfs
def main():
    jug1_capacity = 4  # capacity of the first jug
    jug2_capacity = 3  # capacity of the second jug
    target_amount = 2  # target amount to measure

    # solve using bfs
    print("solving using bfs:")
    bfs_solution = bfs_water_jug(jug1_capacity, jug2_capacity, target_amount)
    if bfs_solution:
        display_steps(bfs_solution)
    else:
        print("no solution found using bfs.")

    print("\nsolving using dfs:")
    # solve using dfs
    dfs_solution = dfs_water_jug(jug1_capacity, jug2_capacity, target_amount)
    if dfs_solution:
        display_steps(dfs_solution)
    else:
        print("no solution found using dfs.")

# run the main function
if __name__ == "__main__":
    main()
