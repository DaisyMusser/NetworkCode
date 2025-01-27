
import networkx as nx
import matplotlib.pyplot as plt


'''
H = nx.path_graph(10)
G = nx.Graph()
G.add_nodes_from([(4, {"color": "red"}), (5, {"color": "green"})])

# does some pretty formatting
subax1 = plt.subplot(121) 

# graphs can be build seperatly and then added together...
G.add_nodes_from(H)

nx.draw(H, with_labels=True, font_weight='bold')
nx.draw(G, with_labels=True, font_weight='bold')

subax2 = plt.subplot(122)
nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
'''

# Figure out how to combine graphs by merging two nodes

G = nx.complete_graph(8)
H = nx.complete_graph(4)

nx.draw(G, with_labels=True)
plt.show()


# nx.draw(H, with_labels=True)



