import random
import time
import matplotlib.pyplot as plt

# Class to represent a disjoint set
class DisjointSet:
    def __init__(self, num_nodes):
        self.parent = [i for i in range(num_nodes)]
        self.rank = [0] * num_nodes

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

# Class to represent a graph
class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.edges = []

    def add_edge(self, src, dest, weight):
        self.edges.append((src, dest, weight))

    def kruskal_algorithm(self):
        mst = Graph(self.num_nodes)
        disjoint_set = DisjointSet(self.num_nodes)
        self.edges = sorted(self.edges, key=lambda edge: edge[2])

        for edge in self.edges:
            src, dest, weight = edge

            src_root = disjoint_set.find(src)
            dest_root = disjoint_set.find(dest)

            if src_root != dest_root:
                mst.add_edge(src, dest, weight)
                disjoint_set.union(src_root, dest_root)

        return mst

def plot_running_time(nodes, kruskal_times):
    plt.plot(nodes, kruskal_times, label='Kruskal Algorithm')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Time (seconds)')
    plt.title('Kruskal Algorithm')
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
    kruskal_times = []

    for num_nodes in range(1, max_nodes + 1):
        graph = generate_graph(num_nodes)

        # Measure running time for Kruskal algorithm
        start_time = time.time()
        graph.kruskal_algorithm()
        end_time = time.time()
        kruskal_times.append(end_time - start_time)

        nodes.append(num_nodes)

    plot_running_time(nodes, kruskal_times)

# Measure running time for graphs with increasing number of nodes (up to 300)
measure_running_time(300)

