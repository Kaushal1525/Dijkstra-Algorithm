import heapq
import numpy as np
import matplotlib.pyplot as plt


def dijkstra(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    distances = {start: 0}

    while open_set:
        current_cost, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in neighbors:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                new_cost = current_cost + 1
                if neighbor not in distances or new_cost < distances[neighbor]:
                    distances[neighbor] = new_cost
                    came_from[neighbor] = current
                    heapq.heappush(open_set, (new_cost, neighbor))

    return None  # No path found


def visualize(grid, path, start, goal):
    grid_np = np.array(grid)
    plt.imshow(grid_np, cmap='gray_r')

    if path:
        for point in path:
            plt.plot(point[1], point[0], 'ro', markersize=5)

    plt.plot(start[1], start[0], 'go', markersize=8, label='Start')
    plt.plot(goal[1], goal[0], 'bo', markersize=8, label='Goal')
    plt.legend()
    plt.show()


# Example usage
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
goal = (4, 4)
path = dijkstra(grid, start, goal)
visualize(grid, path, start, goal)
