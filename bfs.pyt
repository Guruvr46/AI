from collections import deque

def bfs(graph, start_node, goal_node):
    visited = set()  # Create a set to track visited nodes
    queue = deque([start_node])  # Use deque to store the queue, initialized with the start node
    visited.add(start_node)  # Add the start node to the visited set

    while queue:  # While there are nodes to process in the queue
        current_node = queue.popleft()  # Remove the node from the left side of the queue
        print(f"Visiting node: {current_node}")  # Print the current node being visited

        if current_node == goal_node:  # If the current node is the goal node
            print(f"Found the goal node: {goal_node}!!")  # Print the success message
            return  # Exit the function when the goal node is found

        for neighbour in graph[current_node]:  # For each neighbor of the current node
            if neighbour not in visited:  # If the neighbor has not been visited yet
                queue.append(neighbour)  # Add the neighbor to the queue for future exploration
                visited.add(neighbour)  # Mark the neighbor as visited

# Example graph as a dictionary
graph = {
    0: [1, 2, 3],
    1: [4, 5],
    2: [],
    3: [6],
    4: [],
    5: [],
    6: []
}

start_node = 0  # Starting node for BFS
goal_node = 5   # The goal node to be found

bfs(graph, start_node, goal_node)  # Call the BFS function
