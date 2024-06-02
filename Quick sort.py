def quicksort(tabs):
    if len(tabs) <= 1: #cas de base (si l etableau est egale a 1 element on retourne le tableau)
        return tabs
    pivot = tabs.pop() # autre cas
    # tabs.pop()  == tabs[len(tabs)-1] recuperer le dernier element du tabs
    print(pivot)
    gauche = []
    droite = []

    droite.append(pivot)

    for nombre in tabs:
        if (nombre < pivot):
            gauche.append(nombre)
        else:
            droite.append(nombre)

    return quicksort(gauche)+quicksort(droite)


tabs = [42, 3, 6, 21, 45, 2, 18, 20];
print(quicksort(tabs))