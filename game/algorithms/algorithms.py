from collections import deque
from heapq import heappush, heappop

def bfs_puzzle(start_state, goal_state):
    def get_neighbors(state):
        neighbors = []
        zero_row, zero_col = [(r, c) for r in range(3) for c in range(3) if state[r][c] == 0][0]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # gore, dole, levo, desno

        for dr, dc in directions:
            new_row, new_col = zero_row + dr, zero_col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = [row[:] for row in state]
                # Zameni prazno polje sa susednim
                new_state[zero_row][zero_col], new_state[new_row][new_col] = (
                    new_state[new_row][new_col],
                    new_state[zero_row][zero_col],
                )
                neighbors.append(new_state)
        return neighbors

    visited = set()
    queue = deque([(start_state, [])])  # (trenutno stanje, lista poteza)

    while queue:
        current_state, path = queue.popleft()
        # Pretvori matricu u tuple za lakše poređenje i smeštanje u set
        state_tuple = tuple(tuple(row) for row in current_state)

        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        if current_state == goal_state:
            return path  # Lista poteza do cilja

        for neighbor in get_neighbors(current_state):
            queue.append((neighbor, path + [neighbor]))

    return None  # Ako ne postoji rešenje

def best_first_search(start_state, goal_state, heuristic):
    def get_neighbors(state):
        neighbors = []
        zero_row, zero_col = [(r, c) for r in range(3) for c in range(3) if state[r][c] == 0][0]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Gore, dole, levo, desno

        for dr, dc in directions:
            new_row, new_col = zero_row + dr, zero_col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = [row[:] for row in state]
                new_state[zero_row][zero_col], new_state[new_row][new_col] = (
                    new_state[new_row][new_col],
                    new_state[zero_row][zero_col],
                )
                neighbors.append(new_state)
        return neighbors

    def linearize(state):
        return tuple(num for row in state for num in row)

    open_set = []
    heappush(open_set, (0, linearize(start_state), start_state, []))  # Dodaj listu koraka
    visited = set()

    while open_set:
        _, identifier, current_state, path = heappop(open_set)

        if identifier in visited:
            continue
        visited.add(identifier)

        if current_state == goal_state:
            return path + [current_state]

        for neighbor in get_neighbors(current_state):
            if linearize(neighbor) not in visited:
                h_value = heuristic(neighbor, goal_state)
                heappush(open_set, (h_value, linearize(neighbor), neighbor, path + [current_state]))

    return None  # Ako nema rešenja


def hamming_heuristic(state, goal):
    return sum(1 for i in range(3) for j in range(3) if state[i][j] != goal[i][j] and state[i][j] != 0)

def a_star_search(start_state, goal_state, heuristic):
    def get_neighbors(state):
        neighbors = []
        zero_row, zero_col = [(r, c) for r in range(3) for c in range(3) if state[r][c] == 0][0]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Gore, dole, levo, desno

        for dr, dc in directions:
            new_row, new_col = zero_row + dr, zero_col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = [row[:] for row in state]
                new_state[zero_row][zero_col], new_state[new_row][new_col] = (
                    new_state[new_row][new_col],
                    new_state[zero_row][zero_col],
                )
                neighbors.append(new_state)
        return neighbors

    def linearize(state):
        return tuple(num for row in state for num in row)

    open_set = []
    heappush(open_set, (0, 0, linearize(start_state), start_state, []))  # Dodaj listu koraka
    visited = {}

    while open_set:
        f_value, g_value, identifier, current_state, path = heappop(open_set)

        if identifier in visited and visited[identifier] <= g_value:
            continue
        visited[identifier] = g_value

        if current_state == goal_state:
            return path + [current_state]

        for neighbor in get_neighbors(current_state):
            neighbor_identifier = linearize(neighbor)
            h_value = heuristic(neighbor, goal_state)
            g_next = g_value + 1
            f_next = g_next + h_value
            heappush(open_set, (f_next, g_next, neighbor_identifier, neighbor, path + [current_state]))

    return None


def manhattan_heuristic(state, goal):
    goal_positions = {num: (r, c) for r, row in enumerate(goal) for c, num in enumerate(row)}
    total_distance = 0
    for r, row in enumerate(state):
        for c, num in enumerate(row):
            if num != 0:  # Preskoči prazno polje
                goal_r, goal_c = goal_positions[num]
                total_distance += abs(r - goal_r) + abs(c - goal_c)
    return total_distance

