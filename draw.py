import read 
import matplotlib.pyplot as plt 
import networkx as nx


def draw(filePath):
    G = read.makeGraph(filePath)
    nx.draw(G)
    plt.show()

draw('./struct_data/csv/test.csv')
