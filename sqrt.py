# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 15:21:17 2021
@original author: gianluca
@student: Wraith (Flavio Fois)
"""

# Creating two variables for the abs function
x = 20
g = 5.0

# Printing the original value of G
print("Valore iniziale di G: ",g)
# Starting the while cycle
while abs(g * g - x) > 0.00001:        # Checking if the absolute value of the formula (g*g-x) is higher than 0.00001
	# Setting a new value of G
	g = 0.5 * (g + x / g)
	# Printing the new value of G
	print(g)

# If the G absolute value is not higher than 0.00001, then the while cycle ends
# Printing the Square Root value of X, aka G
print("La radice quadrata di", x, "e'", g)