"""
La una lista chiama listaA (fate voi i valori) è composta da numeri e stringhe, si vogliono ordinare gli elementi di a in modo che:

1) i numeri precedano le stringhe
2) i numeri siano ordinati dal più piccolo al più grande
3) le stringhe siano ordinate da quella più corta a quella più lunga
"""

def listaSorter(listaA):
    miniListaB = []
    miniListaC = []
    miniListaD= []
    for i in listaA:
        if type(i) is int:
            miniListaB.append(i)
        elif type(i) is str:
            miniListaC.append(i)
        else:
            miniListaD.append(i)    
    miniListaB.sort()
    miniListaC.sort(key=len)
    miniListaD.sort()
    return miniListaB + miniListaC + miniListaD

print(listaSorter([7, 23, 5, "ciao", 1, "istanza", "bob",  69, "credenziali"]))