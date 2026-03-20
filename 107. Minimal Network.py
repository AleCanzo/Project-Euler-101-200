import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def create_graph(M):
    G = nx.Graph()
    n = 0
    for i in range(40):
        for j in range(i, 40):
            if M[i][j]!=0:
                G.add_node(n)
                G.add_edge(i,j, weight=M[i][j])
                #print(i, j)
    return G
            
def plot_graph(G):
    pos = nx.spring_layout(G, seed=7)
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)    
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()
    return
 
def maximum_saving(G):
    MST = nx.minimum_spanning_tree(G)
    s = 0
    for (u, v, d) in G.edges(data=True):
        s += d["weight"]
    s_mst = 0
    for (u, v, d) in MST.edges(data=True):
        s_mst += d["weight"]
    return s - s_mst    
    
if __name__ == "__main__":
    M = np.loadtxt("101-200/0107_network.txt", dtype=str, delimiter=",")
    M[M == '-'] = '0'  
    M = M.astype(int)
    print(M)
    G = create_graph(M)
    print(maximum_saving(G))
    