
# import matplotlib.pyplot library
import matplotlib.pyplot as plt

# import networkx library
import networkx as nx

# create an empty graph
G = nx.Graph()

# add some nodes
G.add_node(0)
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)

# add some edges
G.add_edge(0, 1)
G.add_edge(2, 1)
G.add_edge(2, 3)
G.add_edge(0, 4)

# draw a graph with red
# node and value edge color
nx.draw(G)
plt.show()

