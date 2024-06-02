import bisect
liste = [62, 7, 42, 16, 40, 24, 31, 4, 11, 9, 27, 1]
def sequenziele(liste, k):

    laenge = len(liste)
    position = 0
    gefunden = False

    while position < laenge and gefunden == False:
        if liste [position]== k:
            ergebnis = "Elemente gefunden an stelle"+ str(position)
            gefunden = True
        else:
            position = position + 1
            ergebnis = "nicht gefunden"
    return ergebnis

k = 42
#print(sequenziele(liste, k))

def binaeresuche(liste ,l,r,k ):# pour ce trie je divise la liste en 2 ca commence a droite ca fini agauvhe
    mitte = (l + r) // 2
    if l > r:
        ergebnis = "kein ergebnis"
        print(ergebnis)
    else:
        if k <liste[mitte]:
            binaeresuche(liste, l, mitte - 1, k)

        if k > liste[mitte]:
            binaeresuche(liste, l,mitte + 1 , k )
        if k == liste[mitte]:
            ergebnis = "erfolgreiche fundstelle an position " + str(mitte)
            print(ergebnis)
suchek = 815
beispieliste = [42, 54, 815, 2323, 10587]
laenge = len(beispieliste)
suche = binaeresuche(beispieliste, 0 , laenge - 1,  suchek)

position = bisect.bisect_left(beispieliste , 7)# linke variante
print("Das elemente wird an position" , str(position))







