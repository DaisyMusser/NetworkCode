import read 
import matplotlib.pyplot as plt 
import networkx as nx
from networkx import drawing 


def draw(filePath):
    G = read.makeGraph(filePath)
    nx.draw(G, pos=nx.spring_layout(G, seed=201))
    plt.show()

draw('./struct_data/csv/test.csv')


