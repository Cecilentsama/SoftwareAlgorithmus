import networkx as nx
import matplotlib.pyplot as plt
import binarytree

#Graph erstellen
neuergraph = nx.Graph()

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

#Kanten hinzufügen
neuergraph.add_edge("STR","FRA")
neuergraph.add_edge("MEM","FRA")
neuergraph.add_edge("BER","FRA")
neuergraph.add_edge("FRA","DOH")
neuergraph.add_edge("FRA","ATL")
neuergraph.add_edge("ATL","HNL")
neuergraph.add_edge("ATL","SFA")
neuergraph.add_edge("DOH","MAL")
neuergraph.add_edge("DOH","PEK")


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