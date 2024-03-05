import random
import networkx as nx
import matplotlib.pyplot as plt
import operator

g = nx.gnp_random_graph(10, 0.5, directed=True)
nx.draw(g, with_labels=True)
plt.show()

x = random.randrange(0, g.number_of_nodes())
# print(x)

counter = {i: 0 for i in range(g.number_of_nodes())}

counter[x] += 1

for _ in range(1000000):
    neighbors = list(g.neighbors(x))
    if len(neighbors) == 0:
        x = random.randrange(0, g.number_of_nodes())
        counter[x] += 1

    else:
        n = random.choice(neighbors)
        counter[n] += 1
        x = n

print(sorted(nx.pagerank(g).items(), key=operator.itemgetter(1), reverse=True))
print(sorted(counter.items(), key=operator.itemgetter(1), reverse=True))