import networkx as nx
import matplotlib.pyplot as plt
import random


G=nx.gnp_random_graph(10,0.5,directed=True)
nx.draw(G)
# plt.show()

x=random.choice([i for i in range(G.number_of_nodes())])
dict_counter={}

for i in range(G.number_of_nodes()):
    dict_counter[i]=0
dict_counter[x] +=1

for i in range(100):
    list_n=list(G.neighbors(x))
    if not list_n:
        x=random.choice([i for i in range(G.numbers_of_nodes)])
        dict_counter[x] +=1
    else:
        x=random.choice(list_n)
        dict_counter[x] +=1


page_rank_by_nx=nx.pagerank(G)
sorted_page_rank_by_nx=sorted(page_rank_by_nx.items(),key=lambda x:x[1])
sorted_dict_counter=sorted(dict_counter.items(),key=lambda x:x[1])

print(sorted_page_rank_by_nx)
print(sorted_dict_counter)