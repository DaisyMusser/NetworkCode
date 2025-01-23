
import json
import networkx as nx
import csv

# for viz
import matplotlib.pyplot as plt

# start of program
# create empty graph
G = nx.Graph()

people = {}
with open("persons_dup_concat.0.csv") as person_file:
    persons_reader = csv.reader(person_file, delimiter=',')
    for row in persons_reader:
		#         persons_reader SCHEMA
        #                                index in lookup 
        # row[0]: person_id
        # row[1]: given_name             [0]
        # row[2]: family_name            [1]
        # row[3]: alternate_spellings    [2]
        # row[4]: occupations            [3]
        # row[5]: orgin_locs      (text) [4]
        # row[6]: residence_locs  (text) [5]
        # row[7]: occupation_locs (text) [6]
        if row[0] != "person_id":
            # if not first row, add to lookup dictionary
            people[row[0]] = (row[1], row[2], row[3], row[4], row[5], row[6], row[7])

with open("arrests.0.csv") as arrest_file:
    arrests_reader = csv.reader(arrest_file, delimiter=',')
    is_first = True
    visited_ids = []
    label_dic = {}
    for row in arrests_reader:
		# 		  arrests_reader SCHEMA 
        # row[0]: object_id     (arrest)
        # row[1]: person_name
        # row[2]: person_id
        # row[3]: location_id   (arrest)
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
                        # use person_lookcup dictionary to get rest of person attributes
                        person_data = people[ID]
                        G.add_node(ID, Full_Name          = name, 
                                       First_Name         = person_data[0], 
                                       Last_Name          = person_data[1], 
                                       Nickname           = person_data[2], 
                                       Occupations        = person_data[3], 
                                       Place_of_Origin    = person_data[4], 
                                       Place_of_Residence = person_data[5], 
                                       Place_of_Work      = person_data[6])
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

# gotta find duplicate people
to_contract = []
for first_id in people.keys():
    for secound_id in people.keys():
        if first_id != secound_id:
            first_matches = False
            # first names
            if people[first_id][0] == people[secound_id][0]:
                first_matches = True
            # secound names
            secound_matches = False
            if people[first_id][1] == people[secound_id][1]:
                secound_matches = True
            # need to combine if dup
            if first_matches and secound_matches:
                to_contract.append((first_id, secound_id))

print(to_contract)

# contract nodes that are probably the same person
for personA, personB in to_contract:
    G = nx.contracted_nodes(G, personA, personB) 

# print(G.number_of_nodes())
# print(label_dic)
nx.draw(G, labels=label_dic, with_labels=True)
plt.show()
# plt.savefig("arrestNetwork.png")

