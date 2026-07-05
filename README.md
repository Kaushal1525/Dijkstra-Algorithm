
# Dijkstra Path Planning Algorithm Visualization

## Overview

This project demonstrates the implementation of Dijkstra's Shortest Path Algorithm for path planning in a two-dimensional grid environment. The algorithm computes the shortest collision-free path between a start position and a goal while avoiding obstacles represented within the grid.

The project also provides a graphical visualization of the computed path using Matplotlib, making it useful for learning graph search algorithms, robot navigation, and autonomous path planning.

---

## Features

- Dijkstra shortest path algorithm
- Grid-based path planning
- Obstacle avoidance
- Shortest path computation
- Path visualization using Matplotlib
- Easy-to-modify grid environment
- Educational implementation for robotics and AI

---

## Technologies Used

- Python 3
- NumPy
- Matplotlib
- Heapq

---

## Project Structure

```text
Dijkstra-Path-Planning/
│
├── dijkstra.py
├── README.md
└── requirements.txt
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Kaushal1525/Dijkstra-Path-Planning.git
```

### Navigate to the project directory

```bash
cd Dijkstra-Path-Planning
```

### Install the required packages

```bash
pip install -r requirements.txt
```

or

```bash
pip install numpy matplotlib
```

---

## Running the Project

Execute the following command:

```bash
python dijkstra.py
```

A visualization window will display the generated grid, obstacles, start node, goal node, and the shortest path.

---

## Working Principle

The algorithm performs the following operations:

1. Initialize the start node with zero cost.
2. Store unexplored nodes in a priority queue.
3. Expand the node with the lowest path cost.
4. Explore neighboring cells.
5. Ignore blocked cells containing obstacles.
6. Update the shortest known distance to neighboring nodes.
7. Continue until the destination is reached.
8. Reconstruct the optimal path from the recorded parent nodes.
9. Display the resulting path graphically.

---

## Grid Representation

```text
0 → Free Cell
1 → Obstacle
```

Example Grid

```text
S X . . .
. X . X .
. . . X .
. X X X .
. . . . G
```

Where:

- **S** = Start Position
- **G** = Goal Position
- **X** = Obstacle
- **.** = Traversable Cell

---

## Visualization

The generated visualization displays:

- Grid map
- Obstacles
- Start node
- Goal node
- Computed shortest path

---

## Algorithm Workflow

```text
Initialize Grid
        │
        ▼
Insert Start Node
        │
        ▼
Priority Queue
        │
        ▼
Expand Lowest-Cost Node
        │
        ▼
Explore Neighboring Cells
        │
        ▼
Update Distances
        │
        ▼
Goal Reached
        │
        ▼
Reconstruct Path
        │
        ▼
Visualize Result
```

---

## Future Enhancements

- Diagonal movement
- Weighted terrain support
- Dynamic obstacle avoidance
- Interactive grid editor
- Animated pathfinding visualization
- ROS integration
- Gazebo simulation
- Autonomous robot navigation
- Multi-goal routing
- Comparison with A*, D* Lite, and Theta* algorithms

---

## Applications

- Autonomous Mobile Robots
- Robot Navigation
- Autonomous Vehicles
- Warehouse Automation
- Drone Navigation
- Intelligent Transportation Systems
- Indoor Navigation
- Artificial Intelligence
- Robotics Education
- Path Planning Research

---

## Requirements

- Python 3.8 or later
- NumPy
- Matplotlib

---

## Dependencies

- numpy
- matplotlib

---

## Author

Kaushal Reddy

AI & Autonomous Systems Engineer

GitHub: https://github.com/Kaushal1525
````
