# Introducir una cadena de caracteres e indicar si es un palíndromo. Una palabra 
# palíndroma es aquella que se lee igual adelante que atrás.

cad = input("Introduce una cadena:")
if cad == cad[::-1]:
	print("Es un palíndromo")
else:
	print("No es un palíndromo")
