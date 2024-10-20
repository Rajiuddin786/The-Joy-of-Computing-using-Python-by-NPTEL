import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

l=[1,2,3,4,5,10,11]

"""Adding Node"""
# G.add_node(1)
# G.add_node(2)
# G.add_node(3)

# G.add_nodes_from(l) #l is a list

"""Adding Edges"""
# G.add_edge(1,2)
# G.add_edge(2,3)
# G.add_edge(1,3)

"""Complete Graph"""
# G=nx.complete_graph(l)

"""Random Graph"""
# G=nx.gnp_random_graph(50,0.3)

"""Scale Free Graph"""
G=nx.barabasi_albert_graph(50,2)
nx.draw(G)
plt.show()

nx.write_gexf(G,"./Files/graph_01.gexf")