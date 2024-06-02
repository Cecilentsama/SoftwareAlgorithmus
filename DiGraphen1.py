import networkx as nx
import matplotlib.pyplot as plt

neuergraph = nx.DiGraph() #Di sind die pfeile

neuergraph.add_node("A")
neuergraph.add_node("B")
neuergraph.add_node("C")
neuergraph.add_node("D")
neuergraph.add_node("E")


neuergraph.add_edge("A","B", weight = 5)
neuergraph.add_edge("B", "C", weight = 7)
neuergraph.add_edge("C","A", weight = 10)
neuergraph.add_edge("C", "D", weight = 5)
neuergraph.add_edge("D", "F", weight = 2)
neuergraph.add_edge("D", "E", weight = 10)
neuergraph.add_edge("E", "A", weight = 10)
neuergraph.add_edge("F","D", weight = 3)


vorlage = nx.spring_layout(neuergraph)
nx.draw(neuergraph, vorlage, with_labels=True)
labels = nx.get_edge_attributes(neuergraph, "weight")
nx.draw_networkx_edge_labels(neuergraph, pos=vorlage, edge_labels=labels)
plt.show()

print(nx.dijkstra_path(neuergraph, "A", "B")) #erste ist der kürzeste weg


print(neuergraph.nodes())

#Alle Kanten ausgeben
print(neuergraph.edges())

nx.draw_networkx(neuergraph)
plt.draw()
plt.show()
#jz kommt stack
import networkx as nx
import matplotlib.pyplot as plt

neuergraph = nx.DiGraph() #Di sind die pfeile

neuergraph.add_node("A")
neuergraph.add_node("B")
neuergraph.add_node("C")
neuergraph.add_node("D")
neuergraph.add_node("E")


neuergraph.add_edge("A","B", weight = 5)
neuergraph.add_edge("B", "C", weight = 7)
neuergraph.add_edge("C","A", weight = 10)
neuergraph.add_edge("C", "D", weight = 5)
neuergraph.add_edge("D", "F", weight = 2)
neuergraph.add_edge("D", "E", weight = 10)
neuergraph.add_edge("E", "A", weight = 10)
neuergraph.add_edge("F","D", weight = 3)


vorlage = nx.spring_layout(neuergraph)
nx.draw(neuergraph, vorlage, with_labels=True)
labels = nx.get_edge_attributes(neuergraph, "weight")
nx.draw_networkx_edge_labels(neuergraph, pos=vorlage, edge_labels=labels)
plt.show()

print(nx.dijkstra_path(neuergraph, "A", "B")) #erste ist der kürzeste weg


print(neuergraph.nodes())

#Alle Kanten ausgeben
print(neuergraph.edges())

nx.draw_networkx(neuergraph)
plt.draw()
plt.show()
