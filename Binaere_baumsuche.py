import binarytree
from binarytree import tree, bst, heap

class Knoten:
    def __init__(self, daten):
        self.links = None
        self.rechts = None
        self.daten = daten

    def hinzufuegen(self, daten):

        if self.daten:
            if daten < self.daten:
                if self.links is None:
                    self.links = Knoten(daten)
                else:
                    self.links.hinzufuegen(daten)
            if daten > self.daten:
                if self.rechts is None:
                    self.rechts = Knoten(daten)
                else:
                    self.rechts.hinzufuegen(daten)
        else:
            self.daten = daten

    def suche(self, k):

        if k < self.daten:
            if self.links is None:
                print("keine Daten gefunden")
            else:
                self.links.suche(k)
        if k > self.daten:
            if self.rechts is None:
                print("keine Daten gefunden")
            else:
                self.rechts.suche(k)
        if k == self.daten:
            print("Datensatz gefunden")
def baumausgabe(knoten):
    if knoten:

        baumausgabe(knoten.links)
        print(knoten.daten)
        baumausgabe(knoten.rechts)


baum = Knoten(98)
baum.hinzufuegen(7)
baum.hinzufuegen(14)
baum.hinzufuegen(10)
baum.hinzufuegen(42)
baum.hinzufuegen(43)
baum.hinzufuegen(8)
baum.hinzufuegen(100)
baum.hinzufuegen(12)
baum.hinzufuegen(32)
baum.hinzufuegen(22)
baum.hinzufuegen(2)
baum.hinzufuegen(1)
baum.hinzufuegen(16)
baum.suche(43)
baumausgabe(baum)

my_tree = tree(height = 2, is_perfect=False)
print(my_tree)


