
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
with open("arrests.0.csv") as csv_file:
    arrests_reader = csv.reader(csv_file, delimiter=',')
	# TODO clean this up...
    # persons_reader = csv.reader(open("persons_dup_concat.csv"), delimiter=',')
    is_first = True
    visited_ids = []
    label_dic = {}
    for row in csv_reader:
		# SCHEMA ~
        # row[0]: object_id (arrest)
        # row[1]: person_name
        # row[2]: person_id
        # row[3]: location_id (arrest)
        # row[4]: location_name (arrest)
        if row[2] != "person_id":
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
						# need to use persons_id to look up other attributes .... in ???
                        G.add_nodes_from([ID], person_name=name)
                        visited_ids.append(ID)
                        # save to dictionary for label lookup when drawing
                        label_dic[ID] = name
                # then make all edges
                for (name, ID_0) in persons_arrested:
                    for (name, ID_1) in persons_arrested:
                        if ID_0 != ID_1:
                            G.add_edge(ID_0, ID_1)
                # start the new arrests 
                arrest_id = row[0]
                persons_arrested = [(row[1], row[2])]
# print(G.number_of_nodes())
# print(label_dic)
nx.draw(G, labels=label_dic, with_labels=True)
plt.show()
# plt.savefig("arrestNetwork.png")

