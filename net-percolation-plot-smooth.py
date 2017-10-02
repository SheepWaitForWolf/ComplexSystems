from pylab import *
import networkx as nx

p = 0.0001
pdata = []
g1data = []
g2data = []
g3data = []

while p < 0.1:
    pdata.append(p)
    g1 = nx.erdos_renyi_graph(100, p)
    g2 = nx.erdos_renyi_graph(500, p)
    g3 = nx.erdos_renyi_graph(1000, p)
    ccs1 = nx.connected_components(g1)
    ccs2 = nx.connected_components(g2)
    ccs3 = nx.connected_components(g3)
    g1data.append(max(len(cc) for cc in ccs1))
    g2data.append(max(len(cc) for cc in ccs2))
    g3data.append(max(len(cc) for cc in ccs3))
    p *= 1.1

subplot(3,1,1)
loglog(pdata, g1data)
xlabel('p')
ylabel('size of largest connected component')

subplot(3,1,2)
loglog(pdata, g2data)
xlabel('p')
ylabel('size of largest connected component')

subplot(3,1,3)
loglog(pdata, g3data)
xlabel('p')
ylabel('size of largest connected component')

show()
