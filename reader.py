import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import arrest
import person

# make an empty graph
G = nx.Graph()

# read csv into df
df = pd.read_csv('./struct_data/csv/arrests.csv')

# add a name column without middle names
df['simple_name'] = df['person_name'].str.replace(r' .* ', ' ', regex=True)

# build graph
ids_of_arrests_made = []
for i, row in df.iterrows():
    # if there is no arrest object for this id yet, make one
    if not row['Object_id'] in ids_of_arrests_made:
        a = arrest.Arrest(row['Object_id'], row['location_id'], row['city_town_village'], row['street'])
        ids_of_arrests_made.append(row['Object_id'])
        G.add_node(a)
    p = person.Person(row['person_name'], row['simple_name'])
    G.add_node(p)
    G.add_edge(a, p)

# now traverse the graph and merge duplicate people
# simple names of every person
names = [p.simple_name for p in G.nodes if isinstance(p, person.Person)]
while len(names) > 0:
    name = names.pop()
    if name in names:
        # we have a duplicate
        # join

# duplicates only rows where folks are repeated
duplicates = df[df['simple_name'].duplicated(keep=False)]
for i, dup_person in duplicates.iterrows():
    print(dup_person['person_name'])

'''
nx.draw(G)
plt.show()
'''
