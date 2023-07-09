import heapq

def a_star(graph, start, goal, heuristic):
    frontier = [(0 + heuristic[start], start)]
    cost = {start: 0}
    parent = {start: None}
    explored = set()

    while frontier:
        (f_score, current_node) = heapq.heappop(frontier)

        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            path.reverse()
            return (path, cost[goal])

        explored.add(current_node)

        for neighbor, neighbor_cost in graph[current_node]:
            tentative_g_score = cost[current_node] + neighbor_cost
            if neighbor in explored:
                if tentative_g_score >= cost.get(neighbor, float('inf')):
                    continue

            if neighbor not in [node[1] for node in frontier] or tentative_g_score < cost.get(neighbor, float('inf')):
                cost[neighbor] = tentative_g_score
                parent[neighbor] = current_node
                heapq.heappush(frontier, (tentative_g_score + heuristic[neighbor], neighbor))

    return None

graph = {
    'A': [('B', 5), ('C', 6)],
    'B': [('D', 4), ('E', 7)],
    'C': [('F', 9), ('G', 8)],
    'D': [('H', 3)],
    'E': [('I', 6)],
    'F': [('J', 5)],
    'G': [('K', 7)],
    'H': [('L', 1)],
    'I': [('M', 2)],
    'J': [('N', 3)],
    'K': [('O', 4)],
    'L': [],
    'M': [],
    'N': [],
    'O': [('P', 1)],
    'P': []
}

heuristic = {
    'A': 10,
    'B': 8,
    'C': 7,
    'D': 6,
    'E': 8,
    'F': 3,
    'G': 2,
    'H': 5,
    'I': 6,
    'J': 3,
    'K': 2,
    'L': 1,
    'M': 4,
    'N': 2,
    'O': 4,
    'P': 0
}

start = input("Enter the start node: ")
goal = input("Enter the goal node: ")

result = a_star(graph, start, goal,heuristic)

if result is not None:
    print(f"The minimum cost from {start} to {goal} is {result}.")
else:
    print(f"There is no path from {start} to {goal}.")
