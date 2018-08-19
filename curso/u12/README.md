# Introducción a las cadenas de caracteres

Las cadenas de caracteres (`str`): Me permiten guardar secuencias de caracteres.

## Definición de cadenas

Podemos definir una cadena de caracteres de distintas formas:

	>>> cad1 = "Hola"
	>>> cad2 = '¿Qué tal?'
	>>> cad3 = '''Hola,
		que tal?'''

## Operaciones básicas con cadenas de caracteres

Algunas de las operaciones que puedo realizar con las cadenas de caracteres son:

* Concatenación: `+`:  El operador + me permite unir datos de tipos secuenciales, en este caso dos cadenas de caracteres.

        >>> "hola " + "que tal"
        'hola que tal'

* Repetición: `*`:  El operador * me permite repetir un dato de un tipo secuencial, en este caso de cadenas de caracteres.

        >>> "abc" * 3
        'abcabcabc'

* Indexación: Puedo obtener el dato de una secuencia indicando la posición en la secuencia. En este caso puedo obtener el caracter de la cadena indicando la posición (**empezando por la posición 0**).

        >>> cadena = "josé"
        >>> cadena[0]
        'j'
        >>> cadena[3]
        'é'

