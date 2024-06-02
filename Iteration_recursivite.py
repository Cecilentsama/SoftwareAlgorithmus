def factorial(n):
    if n == 0:
        return 1
    else:
        print("factorial(" + str(n) + ") = " + str(n) + " * factorial(" + str(n-1) + ")" )
        return n * factorial(n-1)

#print(factorial(5))
def summation(n, result=""):
    if n == 0:
        print(result + "0 = ", end="")
        return 0
    else:
        return n + summation(n-1, result + str(n) + " + ")

print(summation(10))


def summationiterativ(n):
    summe = 0
    for i in range(1,n+1):
        summe += i
    return summe

def summe_iterativ(n):
    summe = 0
    for i in range(1, n+1):
        summe +=i
        print("zwischenergebnis:", i, summe)
    return summe


def summe_rekursiv(n, summe=0):
    if n == 0:
        return summe
    else:
        summe += n
        print("zwischenergebnis" , n, summe)
        return summe_rekursiv(n-1, summe)
print(summe_iterativ(5))
print(summe_rekursiv(5))