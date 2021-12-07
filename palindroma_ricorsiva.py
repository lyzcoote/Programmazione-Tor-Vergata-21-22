"""
Exercise: write a recursive function that returns True if and only if the input string is palindroma
Eserciso: scrivere una funzione ricorsiva che fa return True se e solo se la stringa inserita è palindroma
"""

def is_palindrome(string):
    """
    Returns True if and only if the input string is palindroma
    Fa rutern di True se e solo se la stringa inserita è palindroma
    """
    if string[::-1] == string:
        return True
    else:
        return False

if __name__ == "__main__":
    print(is_palindrome(input("Inserisci la stringa: ")))