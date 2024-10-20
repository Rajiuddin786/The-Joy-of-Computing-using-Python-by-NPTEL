import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

G=nx.Graph()
G=nx.read_edgelist('./Files/facebook_combined.txt')
N=list(G.nodes())

spll=[] #Shortest Path Length List

for u in N:
    for v in N:
        if u != v:
            l=nx.shortest_path_length(G,u,v)
            #print("Shortest path between",u,"and",v,"is:",l)
            spll.append(l)

min_spll = min(spll)
max_spll = max(spll)

avg_spll = np.average(spll)

print("Minimum Shortest Path Lenght:",min_spll)
print("Maximum Shortest Path Lenght:",max_spll)
print("Average Shortest Path Lenght:",avg_spll)

nx.draw(G)
plt.show()