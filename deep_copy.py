"""
Exercise/Esercizio:
Write a Python function called deep_copy that clones the input string and all nested strings it contains.
Scrivere una funzione Python denominata deep_copy che clona la stringa in input e tutte le stringhe annidate che essa contiene.
"""

def deep_copy(s):
    """
    :param s: string to be cloned | prende in input la stringa da clonare
    :return: deep copy of string | fa return della copia profonda della stringa
    """
    if isinstance(s, str): # se s e' una stringa
        return s[:] # ritorna una copia profonda della stringa
    elif isinstance(s, list): # se s e' una lista
        return [deep_copy(i) for i in s] # ritorna una copia profonda della lista
    elif isinstance(s, dict): # se s e' un dizionario
        return {k: deep_copy(v) for k, v in s.items()} # ritorna una copia profonda del dizionario
    else: # se s e' un altro tipo di dato
        return s # ritorna il dato originale

def move_max_new( a ):
    '''
    pre: a e' una lista di numeri
    crea una nuova lista contenente tutti gli
    elementi di a, il massimo deve trovarsi in fondo
    '''
    #a_copy = a[:] # clonazione
    a_copy = a #crea un alias
    n = len(a_copy)
    for i in range(n-1):
        # confrontiamo l'elemento in posizione i e i+1
        if a_copy[i] > a_copy[i+1]:
            # scambio gli elementi
            a_copy[i], a_copy[i+1] = \
                a_copy[i+1], a_copy[i]
            
    return a_copy

if __name__ == '__main__':
    print("Printing original list:")
    print(['a', 'b', ['c', 'd'], {'e': 'f'}])
    print("\n")
    print("Using Deep Copy")
    print(deep_copy(['a', 'b', ['c', 'd'], {'e': 'f'}]))
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    c = move_max_new(b)
    print("\nPrinting c values using Move Max")
    print(c)
    print("\nPrinting original b values")
    print(b)
    id(b)