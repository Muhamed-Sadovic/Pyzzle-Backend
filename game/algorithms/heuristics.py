def manhattan_heuristic(state, goal):
    goal_positions = {num: (r, c) for r, row in enumerate(goal) for c, num in enumerate(row)}
    total_distance = 0
    for r, row in enumerate(state):
        for c, num in enumerate(row):
            if num != 0:
                goal_r, goal_c = goal_positions[num]
                total_distance += abs(r - goal_r) + abs(c - goal_c)
    return total_distance

def hamming_heuristic(state, goal):
    return sum(1 for i in range(3) for j in range(3) if state[i][j] != goal[i][j] and state[i][j] != 0)