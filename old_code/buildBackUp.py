
import networkx as nx
import csv

# for viz
import matplotlib.pyplot as plt

# start of program
# create empty graph
G = nx.Graph()

# TODO: want to have all person data saved as node attributes. Format:
# G.add_nodes_from([(node_int_id, {"field_name0": "data0"
#                                  "field_name1": "data1"
#                                  "field_name2": "data2"})])
with open("arrests.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    is_first = True
    for row in csv_reader:
        # row[0]: object_id (arrest)
        # row[1]: person_name
        # row[2]: person_id
        if is_first:
            # start of first arrest processed 
            arrest_id = row[0]
            persons_arrested = [row[2]]
            is_first = False
        elif arrest_id == row[0]:
            # next person in current arrest
            persons_arrested.append(row[2])
        elif arrest_id != row[0]:
            # start of new arrest again
            # make edges between list of persons_arrested
            for person_id0 in persons_arrested:
                for person_id1 in persons_arrested:
                    if person_id0 != person_id1:
                        G.add_edge(person_id0, person_id1)
            # clear out persons_arrested
            persons_arrested = [row[2]]
            # start the new arrests 
            arrest_id = row[0]
print(G.number_of_nodes())
# nx.draw(G)
# plt.show()
# plt.savefig("arrestNetwork.png")

