import networkx as nx
import matplotlib.pyplot as plt

# Create the graph Unbalanced:
G = nx.Graph()

# Add the nodes
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17])

# Add the edges
G.add_edges_from([(1, 2), (1, 3), (1, 5), (2, 4), (2, 10), (3, 6), (3, 7), (3, 12), (4, 11), (5, 7), (5, 12), (5, 10), (6, 13), (7, 8), (7, 12), (8, 9), (9, 15), (11, 17), (13, 15), (13, 16)])

# Set the position of each node
pos = {1: (0, 0), 2: (-1, -1), 3: (1, -1), 4: (-2, -2), 5: (0, -2), 6: (2, -2), 7: (-1, -3), 8: (0, -4), 9: (1, -5), 10: (-2, -3), 11: (-3, -4), 12: (0, -3), 13: (2, -3), 15: (1, -6), 16: (2, -4), 17: (-4, -3)}

# Draw the graph
nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos, font_size=12)
plt.axis("off")
plt.show()

