import networkx as nx
import numpy as np

g = nx.read_edgelist("facebook_combined.txt")
n = nx.nodes(g)

spll = []

for node1 in n:
    for node2 in n:
        if node1 != node2:
            shortest_path = nx.shortest_path(g, node1, node2)
            spll.append(shortest_path)
            print(f"The shortest path for {node1} to {node2} is {shortest_path}")

print("The min short path:", min(spll))
print("The max short path:", max(spll))
print("The avg short path:", np.average(spll))