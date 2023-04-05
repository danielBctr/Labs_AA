import networkx as nx
import matplotlib.pyplot as plt
import time

# Create the graph, Balanced:
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 16, 17, 18, 19])
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 10), (4, 11), (5, 12), (5, 13), (6, 16), (7, 17), (10, 18), (10, 19), (11, 18), (11, 19)])

# Set the position of each node
pos = {1: (0, 0), 2: (-1, -1), 3: (1, -1), 4: (-2, -2), 5: (0, -2), 6: (2, -2), 7: (-1, -3), 10: (-3, -3), 11: (-2, -4), 12: (0, -3), 13: (2, -3), 16: (3, -2), 17: (-4, -3), 18: (-3, -4), 19: (-2, -5)}

# Define the DFS function
def dfs(graph, start, goal, limit, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    if start == goal:
        return visited
    if limit == 0:
        return None
    for neighbor in graph[start]:
        if neighbor not in visited:
            path = dfs(graph, neighbor, goal, limit-1, visited)
            if path is not None:
                return path
    return None

# Define the BFS function
def bfs(graph, start, goal):
    visited = set()
    queue = [(start, [start])]

    while queue:
        (vertex, path) = queue.pop(0)

        if vertex not in visited:
            visited.add(vertex)

            if vertex == goal:
                return path

            for neighbor in graph[vertex]:
                queue.append((neighbor, path + [neighbor]))

    return None

# Define a function to run the search algorithms
def run_searches(graph, start, goals, limit):
    dfs_times = []
    bfs_times = []
    dfs_nodes_visited = []
    bfs_nodes_visited = []

    for goal in goals:
        start_time = time.time()
        dfs_result = dfs(graph, start, goal, limit)
        end_time = time.time()
        dfs_time = end_time - start_time
        dfs_times.append(dfs_time)
        if dfs_result is not None:  # Check if dfs_result is not None
            dfs_nodes_visited.append(len(dfs_result))
        else:
            dfs_nodes_visited.append(0)

        start_time = time.time()
        bfs_result = bfs(graph, start, goal)
        end_time = time.time()
        bfs_time = end_time - start_time
        bfs_times.append(bfs_time)
        if bfs_result is not None:  # Check if bfs_result is not None
            bfs_nodes_visited.append(len(bfs_result))
        else:
            bfs_nodes_visited.append(0)

    return dfs_nodes_visited, bfs_nodes_visited, dfs_times, bfs_times



# Set the search
start = 1
goals = [4, 7, 3, 13, 16, 17]
limit = 100
#Run the search algorithms

dfs_nodes_visited, bfs_nodes_visited, dfs_times, bfs_times = run_searches(G, start, goals, limit)
#Create the bar plot

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.bar(['Goal '+str(i) for i in goals], dfs_nodes_visited, color='b')
plt.title('DFS Nodes Visited, Balanced')
plt.xlabel('Goal Node')
plt.ylabel('Number of Nodes Visited')

plt.subplot(1, 2, 2)
plt.bar(['Goal '+str(i) for i in goals], bfs_nodes_visited, color='g')
plt.title('BFS Nodes Visited, Balanced')
plt.xlabel('Goal Node')
plt.ylabel('Number of Nodes Visited')

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.bar(['Goal '+str(i) for i in goals], dfs_times, color='b')
plt.title('DFS Time Taken, Balanced')
plt.xlabel('Goal Node')
plt.ylabel('Time (seconds)')

plt.subplot(1, 2, 2)
plt.bar(['Goal '+str(i) for i in goals], bfs_times, color='g')
plt.title('BFS Time Taken, Balanced')
plt.xlabel('Goal Node')
plt.ylabel('Time (seconds)')

plt.tight_layout()
plt.show()

# Create the bar plot
plt.figure(figsize=(15, 5))

# Nodes Visited Subplot
plt.subplot(1, 2, 1)
bar_width = 0.35
r1 = range(len(goals))
r2 = [x + bar_width for x in r1]
plt.bar(r1, dfs_nodes_visited, color='b', width=bar_width, label='DFS')
plt.bar(r2, bfs_nodes_visited, color='g', width=bar_width, label='BFS')
plt.title('Nodes Visited Comparison, Balanced')
plt.xticks([r + bar_width/2 for r in r1], ['Goal '+str(i) for i in goals])
plt.xlabel('Goal Node')
plt.ylabel('Number of Nodes Visited')
plt.legend()

# Time Taken Subplot
plt.subplot(1, 2, 2)
plt.bar(r1, dfs_times, color='b', width=bar_width, label='DFS')
plt.bar(r2, bfs_times, color='g', width=bar_width, label='BFS')
plt.title('Time Taken Comparison, Balanced')
plt.xticks([r + bar_width/2 for r in r1], ['Goal '+str(i) for i in goals])
plt.xlabel('Goal Node')
plt.ylabel('Time (seconds)')
plt.legend()

plt.tight_layout()
plt.show()

