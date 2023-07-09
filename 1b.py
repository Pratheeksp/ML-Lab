import heapq

def best_first_search(graph, start, goal):
    frontier = [(0, start)]
    explored = set()

    while frontier:
        (cost, current_node) = heapq.heappop(frontier)

        if current_node == goal:
            return cost

        explored.add(current_node)
        print(f"Explored node: {current_node}")

        for neighbor, neighbor_cost in graph[current_node]:
            if neighbor not in explored and neighbor not in [node[1] for node in frontier]:
                heapq.heappush(frontier, (neighbor_cost+cost, neighbor))
                print(f"Added node {neighbor} to frontier with cost {neighbor_cost}")

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

start = input("Enter the start node: ")
goal = input("Enter the goal node: ")

result = best_first_search(graph, start, goal)

if result is not None:
    print(f"The minimum cost from {start} to {goal} is {result}.")
else:
    print(f"There is no path from {start} to {goal}.")
     