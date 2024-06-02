import networkx as nx
import matplotlib.pyplot as plt

#Graph erstellen
neuergraph = nx.DiGraph()

#Knoten erstellen
neuergraph.add_node("STR")
neuergraph.add_node("MEM")
neuergraph.add_node("BER")
neuergraph.add_node("FRA")
neuergraph.add_node("ATL")
neuergraph.add_node("DOH")
neuergraph.add_node("HNL")
neuergraph.add_node("SFA")
neuergraph.add_node("PEK")
neuergraph.add_node("MAL")

#Kanten hinzufÃ¼gen
neuergraph.add_edge("STR","FRA", weight = 10)
neuergraph.add_edge("FRA","STR", weight = 10)
neuergraph.add_edge("MEM","FRA", weight = 15)
neuergraph.add_edge("FRA","MEM", weight = 15)
neuergraph.add_edge("BER","FRA", weight = 40)
neuergraph.add_edge("FRA","BER", weight = 40)
neuergraph.add_edge("FRA","DOH", weight = 200)
neuergraph.add_edge("DOH","FRA", weight = 200)
neuergraph.add_edge("FRA","ATL", weight = 300)
neuergraph.add_edge("ATL","FRA", weight = 300)
neuergraph.add_edge("ATL","HNL", weight = 150)
neuergraph.add_edge("HNL","ATL", weight = 150)
neuergraph.add_edge("ATL","SFA", weight = 80)
neuergraph.add_edge("SFA","ATL", weight = 80)
neuergraph.add_edge("DOH","MAL", weight = 100)
neuergraph.add_edge("MAL","DOH", weight = 100)
neuergraph.add_edge("DOH","PEK", weight = 250)
neuergraph.add_edge("PEK","DOH", weight = 250)
neuergraph.add_edge("DOH","ATL",weight=500)
neuergraph.add_edge("ATL","DOH",weight=500)



vorlage = nx.spring_layout(neuergraph)
nx.draw(neuergraph, vorlage, with_labels=True)
labels = nx.get_edge_attributes(neuergraph, "weight")
nx.draw_networkx_edge_labels(neuergraph, pos=vorlage, edge_labels=labels)
plt.show()

print(nx.dijkstra_path(neuergraph, "STR", "HNL"))

#Alle Knoten ausgeben
print(neuergraph.nodes())

#Alle Kanten ausgeben
print(neuergraph.edges())

#entfernen
#neuergraph.remove_node(6)
#print(neuergraph.nodes())

#entfernen
#neuergraph.remove_edge(1, 4)
#print(neuergraph.edges())

#anzahl knoten
#print(neuergraph.number_of_nodes())

#anzahl kanten
#print(neuergraph.number_of_edges())

#print(neuergraph.degree(1))

nx.draw_networkx(neuergraph)
plt.draw()
plt.show()