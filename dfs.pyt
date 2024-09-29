def dfs(graph, start_node, goal_node):
    visited = set()  # Create a set to track visited nodes
    stack = [start_node]  # Use a stack (LIFO) initialized with the start node
    visited.add(start_node)  # Mark the start node as visited

    while stack:  # While there are nodes in the stack
        current_node = stack.pop()  # Pop the last added node (LIFO behavior)
        print(f"Visiting node: {current_node}")  # Print the current node being visited

        if current_node == goal_node:  # If the current node is the goal node
            print(f"Found the goal node: {goal_node}!!")  # Print success message
            return  # Exit the function when the goal node is found

        for neighbour in graph[current_node]:  # For each neighbor of the current node
            if neighbour not in visited:  # If the neighbor has not been visited
                stack.append(neighbour)  # Push the neighbor onto the stack
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

start_node = 0  # Starting node for DFS
goal_node = 5   # The goal node to be found

dfs(graph, start_node, goal_node)  # Call the DFS function
