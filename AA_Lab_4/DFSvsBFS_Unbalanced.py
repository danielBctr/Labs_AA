import networkx as nx
import matplotlib.pyplot as plt
import time

# Create the graph, Unbalanced:
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17])
G.add_edges_from([(1, 2), (1, 3), (1, 5), (2, 4), (2, 10), (3, 6), (3, 7), (3, 12), (4, 11), (5, 7), (5, 12), (5, 10), (6, 13), (7, 8), (7, 12), (8, 9), (9, 15), (11, 17), (13, 15), (13, 16)])

# Set the position of each node
pos = {1: (0, 0), 2: (-1, -1), 3: (1, -1), 4: (-2, -2), 5: (0, -2), 6: (2, -2), 7: (-1, -3), 8: (0, -4), 9: (1, -5), 10: (-2, -3), 11: (-3, -4), 12: (0, -3), 13: (2, -3), 15: (1, -6), 16: (2, -4), 17: (-4, -3)}

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
        dfs_nodes_visited.append(len(dfs_result))

        start_time = time.time()
        bfs_result = bfs(graph, start, goal)
        end_time = time.time()
        bfs_time = end_time - start_time
        bfs_times.append(bfs_time)
        bfs_nodes_visited.append(len(bfs_result))

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
plt.title('DFS Nodes Visited, Unbalanced')
plt.xlabel('Goal Node')
plt.ylabel('Number of Nodes Visited')

plt.subplot(1, 2, 2)
plt.bar(['Goal '+str(i) for i in goals], bfs_nodes_visited, color='g')
plt.title('BFS Nodes Visited,Unbalanced')
plt.xlabel('Goal Node')
plt.ylabel('Number of Nodes Visited')

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.bar(['Goal '+str(i) for i in goals], dfs_times, color='b')
plt.title('DFS Time Taken,Unbalanced')
plt.xlabel('Goal Node')
plt.ylabel('Time (seconds)')

plt.subplot(1, 2, 2)
plt.bar(['Goal '+str(i) for i in goals], bfs_times, color='g')
plt.title('BFS Time Taken,Unbalanced')
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
plt.title('Nodes Visited Comparison, Unbalanced')
plt.xticks([r + bar_width/2 for r in r1], ['Goal '+str(i) for i in goals])
plt.xlabel('Goal Node')
plt.ylabel('Number of Nodes Visited')
plt.legend()

# Time Taken Subplot
plt.subplot(1, 2, 2)
plt.bar(r1, dfs_times, color='b', width=bar_width, label='DFS')
plt.bar(r2, bfs_times, color='g', width=bar_width, label='BFS')
plt.title('Time Taken Comparison, Unbalanced')
plt.xticks([r + bar_width/2 for r in r1], ['Goal '+str(i) for i in goals])
plt.xlabel('Goal Node')
plt.ylabel('Time (seconds)')
plt.legend()

plt.tight_layout()
plt.show()

