def palindroma(a):
    b = a[::-1]        # Inverso dell'input dato
    if a == b:
        return True
    else:
        return False

if palindroma(input("Dammi una parola: ")):
    print("La stringa che hai inserito è palindroma")
else:
    print("La stringa che hai inserito non è palindroma")