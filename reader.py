import pandas as pd
import networkx as nx

# make an empty graph
G = nx.Graph()

# read csv into df
df = pd.read_csv('./struct_data/csv/arrests.csv')

# add a name column without middle names
df['simple_name'] = df['person_name'].str.replace(r' .* ', ' ', regex=True)

# duplicates only rows where folks are repeated
# will be used to connect in graph later on ....
duplicates = df[df['simple_name'].duplicated(keep=False)]

# build graph
# for each arrest
# make a graph of everyone in that arrest, connected
# then combine graphs by merging nodes that represent the same person (probably)

# use this format to add nodes with attributes...
# G.add_nodes_from([(4, {"color": "red"}), (5, {"color": "green"})])


