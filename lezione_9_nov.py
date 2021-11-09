"""
Lezione 9 Novembre 2021
"""

x = float(input('Inserisci il valore di X: '))
y = float(input('Inserisci il valore di Y: '))


def radice_quadrata(a):
    g = 5.0
    while abs(g * g - a) > 0.00001:
        g = 0.5 * (g + a/g)
    return g

r_x, r_y = radice_quadrata(x), radice_quadrata(y)

print('La radice quadrata di X è:', r_x)
print('La radice quadrata di Y è:', r_y)
print('La radice quadrata di X + Y è:', r_x + r_y)