import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph Balanced:
G = nx.DiGraph()

# Add nodes to the graph
G.add_node(1)
G.add_nodes_from([2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 16, 17, 18, 19])

# Add edges to the graph
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 10), (4, 11), (5, 12), (5, 13), (6, 16), (7, 17), (7, 18), (7, 19)])

# Define positions for the nodes
pos = {1: (0, 0), 2: (-1, -1), 3: (1, -1), 4: (-2, -2), 5: (0, -2), 6: (2, -2), 7: (4, -2), 10: (-3, -4), 11: (-1, -4), 12: (1, -4), 13: (3, -4), 16: (2, -6), 17: (4, -6), 18: (6, -6), 19: (8, -6)}

# Draw the graph with node labels and positions
nx.draw(G, pos, with_labels=True, node_size=500)

# Show the graph
plt.show()

