# Tipo de datos booleanos

## Tipo booleano

El tipo booleano o lógico se considera en python3 como un subtipo del tipo entero. Se puede representar dos valores: verdadero o false (True, False).

## ¿Qué valores se interpretan como FALSO?

Cuando se evalúa una expresión, hay determinados valores que se interpretan como False:

* `False`
* Cualquier número 0. (0, 0.0)
* Cualquier secuencia vacía ([], (), '')
* Cualquier diccionario vacío ({})

## Operadores booleanos o lógicos

Los operadores booleanos se utilizan para operar sobre expresiones booleanas y se suelen utilizar en las estructuras de control alternativas (if, while):

* `x or y`: Si x es falso entonces y, sino x. Este operados sólo evalúa el segundo argumento si el primero es False.
* `x and y`: Si x es falso entonces x, sino y. Este operados sólo evalúa el segundo argumento si el primero es True.
* `not x`: Si x es falso entonces True, sino False.

## Operadores de comparación

Los operadores de comparación, me permiten comparar dos valores y devuelven un valor booleano, dependiendo de lo que este comparando.

`== != >= > <= <`
