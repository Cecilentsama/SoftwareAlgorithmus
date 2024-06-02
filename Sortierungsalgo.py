def bubblesort(beispielarray):
    #beispielarray = [98, 7, 14, 10, 42, 43, 8, 100, 12, 32, 22, 2, 1, 16]
    n = len(beispielarray)
    for i in range(n-1):
        for j in range(n-i-1):
            if beispielarray[j] > beispielarray[j+1]:
                beispielarray[j],beispielarray[j+1] = beispielarray[j+1],beispielarray[j]
    return beispielarray
beispielarray = [98, 7, 14, 10, 42, 43, 8, 100, 12, 32, 22, 2, 1, 16]
print(bubblesort(beispielarray))
