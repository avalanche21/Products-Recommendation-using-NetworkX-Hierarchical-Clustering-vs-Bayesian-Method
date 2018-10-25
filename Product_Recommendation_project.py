# libraries
import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

data = pd.read_csv('TransactionData.csv')
print(data)
data = data

# find the unique nodes from DataFrame
a = data["ItemType"].tolist()
print("unique nodes")
print(np.unique(a))
unique_nodes = np.unique(a)

# construct df2
# it contains the
# which we will use it as an edges data and
# then we will collapse the frequency into the wight of the graph in the Bi-directional graph (Multi-graph)
df2 = pd.DataFrame(columns = ['TransactionID','From','To'])
print(df2)
x = len(data['TransactionID'])
print("Show table length", x)
j=0

list_TransactionID1 = list(data['TransactionID'])
list_ItemType1 = list(data['ItemType'])
print(list_TransactionID1)
print(list_ItemType1)

list_TransactionID2 = []
list_From2 = []
list_To2= []

x = len(list_TransactionID1)
for i in range(0,x-1):
    if list_TransactionID1[i] == list_TransactionID1[i+1]:
        list_TransactionID2.append(list_TransactionID1[i])
        list_From2.append(list_ItemType1[i])
        list_To2.append(list_ItemType1[i+1])

print(len(list_TransactionID2))
print(len(list_From2))
print(len(list_To2))

combined = [('TransactionID', list_TransactionID2),
         ('From', list_From2),
         ('To', list_To2)]
df2 = pd.DataFrame.from_items(combined)
del combined
del list_From2
del list_To2
print(df2)

# First, we go with MultiGraph (we will use Graph later)
G= nx.from_pandas_edgelist(df2, 'From', 'To',
                           edge_attr='TransactionID'
                     , create_using=nx.MultiGraph())

# To save time, you don't need to print this
# #print(len(G))
# print(G.nodes())
# print(G.edges(data=True))
# #Draw the graph showing the Item names (Nodes) and Transaction ID (Attributes)
# edge_labels = nx.get_edge_attributes(G,'TransactionID')
# pos = nx.spring_layout(G)
# nx.draw(G,pos, with_labels=True)
# nx.draw_networkx_edge_labels(G,pos, labels = edge_labels)
# # show the network graph
# plt.show()
#############################################

# Show total number of edges between 2 nodes
print(G.number_of_edges(unique_nodes[1], unique_nodes[2]))
# Now let's see number of edges between every nodes
total_count = 0
k = len(unique_nodes)

# Lists L1 and L2, count will be used later on
L1 = []
L2 = []
count=[]
for j in range(0,k-1):
    count.append(0)
    L1.append(unique_nodes[j])
    L2.append(unique_nodes[j])
    for i in range(1,k-j):
        print("show number of connections from node: ", str(unique_nodes[j]), "to node: ", str(unique_nodes[j+i]))
        print(G.number_of_edges(unique_nodes[j], unique_nodes[j+i]))
        count.append(G.number_of_edges(unique_nodes[j], unique_nodes[j+i]))
        L1.append(unique_nodes[j])
        L2.append(unique_nodes[j+i])
count.append(0)
L1.append(unique_nodes[k-1])
L2.append(unique_nodes[k-1])
print("show total count: ", sum(count))
# now construct Edge Data !
# Let's create a new DataFrame storing only the count of the product being bought together
# store those values in the edge between 2 nodes
combined = [('Item1', L1),
         ('Item2', L2),
         ('Count', count)]
df3 = pd.DataFrame.from_items(combined)
print(L1)
print(L2)
print(df3)
GG= nx.from_pandas_edgelist(df3, 'Item1', 'Item2',
                           edge_attr='Count'
                     , create_using=nx.Graph())
print(len(GG))
print(GG.nodes())
print(GG.edges(data=True))
#Draw the graph showing the City Names (Nodes) and Distances (Attributes)
#edge_labels = nx.get_edge_attributes(G,'distance')
edge_labels = nx.get_edge_attributes(GG,'Count')
pos = nx.spring_layout(GG, scale=0.5)
nx.draw(GG,pos, with_labels=True)
nx.draw_networkx_edge_labels(GG,pos, labels = edge_labels)
# show the network graph
plt.show()


# export distance dataframe to a csv file
df3.to_csv('df3.csv')