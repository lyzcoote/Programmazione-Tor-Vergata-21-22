"""
Lezione 9 Novembre 2021
"""

x = float(input('Inserisci il valore di X: '))
y = float(input('Inserisci il valore di Y: '))

g_x = 5.0

while abs(g_x * g_x - x) > 0.00001:
    g_x = 0.5 * (g_x + x/g_x)

g_y = 5.0

while abs(g_y * g_y - y) > 0.00001:
    g_y = 0.5 * (g_y + y/g_y)

print('La radice quadrata di X è:', g_x)
print('La radice quadrata di Y è:', g_y)
print('La radice quadrata di X + Y è:', g_x + g_y)