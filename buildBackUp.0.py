
import networkx as nx
import csv

# for viz
import matplotlib.pyplot as plt

# start of program
# create empty graph
G = nx.Graph()

# TODO 66 nodes/individulas right now, should be 67
#      print all names to see who's missing
#      noooo put on nodes!!
with open("arrests.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    is_first = True
    visited_ids = []
    label_dic = {}

    # for debugging
    count = 0
    for row in csv_reader:
        # row[0]: object_id (arrest)
        # row[1]: person_name
        # row[2]: person_id
        if is_first:
            # start of first arrest processed 
            arrest_id = row[0]
            persons_arrested = [(row[1], row[2])]
            is_first = False
        elif arrest_id == row[0]:
            # next person in current arrest
            persons_arrested.append((row[1], row[2]))
        elif arrest_id != row[0]:
            # start of new arrest again
            # first make all nodes
            for (name, ID) in persons_arrested:
                if not ID in visited_ids:
                    # TODO attach other data/objects here!
                    G.add_nodes_from([ID], person_name=name)
                    visited_ids.append(ID)
                    # save to dictionary for label lookup when drawing
                    label_dic[ID] = name
                    count += 1
            # then make all edges
            for (name, ID_0) in persons_arrested:
                for (name, ID_1) in persons_arrested:
                    if ID_0 != ID_1:
                        G.add_edge(ID_0, ID_1)
            # start the new arrests 
            arrest_id = row[0]
            persons_arrested = [(row[1], row[2])]
print(G.number_of_nodes())
print(count)
nx.draw(G, labels=label_dic, with_labels=True, font_weight='bold')
plt.show()
# plt.savefig("arrestNetwork.png")

