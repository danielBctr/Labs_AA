import random
import time
from matplotlib import pyplot as plt
# Class to represent a graph
class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.graph = [[0] * num_nodes for _ in range(num_nodes)]

    def add_edge(self, src, dest, weight):
        self.graph[src][dest] = weight
        self.graph[dest][src] = weight

    def get_min_key(self, key, mst_set):
        min_val = float('inf')
        min_idx = -1

        for v in range(self.num_nodes):
            if key[v] < min_val and mst_set[v] == False:
                min_val = key[v]
                min_idx = v

        return min_idx

    def prim_algorithm(self):
        parent = [-1] * self.num_nodes
        key = [float('inf')] * self.num_nodes
        mst_set = [False] * self.num_nodes

        key[0] = 0
        parent[0] = -1

        for _ in range(self.num_nodes):
            u = self.get_min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.num_nodes):
                if self.graph[u][v] > 0 and mst_set[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        mst = Graph(self.num_nodes)

        for v in range(1, self.num_nodes):
            mst.add_edge(parent[v], v, self.graph[parent[v]][v])

        return mst

def plot_running_time(nodes, prim_times):
    plt.plot(nodes, prim_times, label='Prim Algorithm')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Time (seconds)')
    plt.title('Prim Algorithm')
    plt.legend()
    plt.show()

# Generate a graph with a given number of nodes
def generate_graph(num_nodes):
    graph = Graph(num_nodes)
    for src in range(num_nodes):
        for dest in range(src + 1, num_nodes):
            weight = random.randint(1, 100)
            graph.add_edge(src, dest, weight)
    return graph

# Vary the number of nodes and measure the running time
def measure_running_time(max_nodes):
    nodes = []
    prim_times = []

    for num_nodes in range(1, max_nodes + 1):
        graph = generate_graph(num_nodes)

        # Measure running time for Prim algorithm
        start_time = time.time()
        graph.prim_algorithm()
        end_time = time.time()
        prim_times.append(end_time - start_time)

        nodes.append(num_nodes)

    plot_running_time(nodes, prim_times)

# Measure running time for graphs with increasing number of nodes (up to 300)
measure_running_time(300)

