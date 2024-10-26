import networkx as nx
import random
import matplotlib.pyplot as plt

def add_edges():
    nodes=list(G.nodes())

    for s in nodes:
        for t in nodes:
            if s!=t:
                r=random.random()
                if r<=0.5:
                    G.add_edge(s,t)
    return G

def assign_points(G):
    nodes=list(G.nodes())
    p=[]
    for node in nodes:
        p.append(100)
    return p

def distribute_points(G,points):
    nodes=list(G.nodes())
    new_points=[]
    for i in range(len(nodes)):
        new_points.append(0)
    for node in nodes:
        out=list(G.out_edges(node))
        if not out:
            new_points[node] += points[node]
        else:
            share=points[node]/len(out)
            for  (src,tar) in out:
                new_points[tar]=new_points[tar]+share
    return new_points

def keep_distributing(points,G):
    for _ in range(100):
        new_points=distribute_points(G,points)
        # print(new_points)
        points=new_points
        # stop=input("Continue y/n").capitalize()
        # if stop == 'N':
        #     break
    return new_points

def rank_by_points(final_points):
    dic_final_point={}
    for i,point in enumerate(final_points):
        dic_final_point[i]=point

    sorted_dic_final_point = sorted(dic_final_point.items(),key=lambda x:x[1])
    return sorted_dic_final_point

G=nx.DiGraph()
G.add_nodes_from([i for i in range(10)])
G=add_edges()

nx.draw(G,with_labels=True)
# plt.show()

points=assign_points(G)

final_points=keep_distributing(points,G)

final_res=rank_by_points(final_points)
print('My Solution')
for i,point in final_res:
    print(f"{i}: {point}")

print("-------------")

print("Solution by Networkx")
final_res_by_nx=nx.pagerank(G)
sorted_final_res_by_nx=sorted(final_res_by_nx.items(),key=lambda x:x[1])
for i,point in sorted_final_res_by_nx:
    print(f"{i}: {point}")