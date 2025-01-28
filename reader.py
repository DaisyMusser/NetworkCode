import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import arrest
import person

# make an empty graph
G = nx.Graph()

# read csv into df
df = pd.read_csv('./struct_data/csv/test.csv')

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

duplicate_rows   = df[df['simple_name'].duplicated(keep=False)]
duplicate_names  = [row['person_name'] for i, row in duplicate_rows.iterrows()]
all_people       = [p for p in G.nodes if isinstance(p, person.Person)]
duplicate_people = [p for p in all_people if p.full_name in duplicate_names]

last_dup = False
for dup in duplicate_people:
    if last_dup:
        G = nx.contracted_nodes(G, last_dup, dup)
    last_dup = dup

nx.draw(G)
plt.show()
