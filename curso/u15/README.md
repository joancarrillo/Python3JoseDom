# Estructura de control: Alternativas

## Alternativa simple

Al ejecutarse la instrucción `if` se evalúa la condición lógica. Si la condición lógica es `True` se ejecutan de manera secuencial el bloque de instrucciones . Si la condición es `False` no se ejecuta el bloque de instrucciones. Una vez ejecutado el `if` (opción verdadera o falsa) se continúa la ejecución de forma secuencial por la siguiente instrucción (bloque de instrucción no identado).

### Ejemplo

Programa que pida la edad y diga si es mayor de edad.

	edad = int(input("Dime tu edad:"))
	if edad>=18:
		print("Eres mayor de edad")
	print("Programa terminado")

## Alternativa doble

Al ejecutarse la instrucción `if` se evalúa la condición lógica. Si la condición lógica es **True** se ejecutan de manera secuencial el primer bloque de instrucciones. Si la condición es `False` se ejecuta el segundo bloque de instrucción.  Una vez ejecutado el `if` (opción verdadera o falsa) se continúa la ejecución de forma secuencial por la siguiente instrucción (bloque de instrucción no identado).

### Ejemplo

Programa que pida la edad y diga si es mayor de edad o menor de edad.

    edad = int(input("Dime tu edad:"))
	if edad>=18:
		print("Eres mayor de edad")
    else:
	    print("Eres menor de edad")
	print("Programa terminado")

## Alternativa múltiple

En este caso tenemos varias opciones. Vamos preguntando por cada una de las opciones y *según* el valor de la expresión ejecutamos un bloque o otro. Esta estructura de control nos permite programar la lógica de la instrucción `Segun` del pseudocódigo.

### Ejemplo

Programa que pide una nota de un examen por teclado y muestra la nota como "Sobresaliente", "Notable", "Bien", "Suficiente", "Suspendido". En pseudocódigo podemos usar la instrucción `Segun`:

	Proceso notas
		Definir nota como entero;
		Escribir "Dime tu nota:";
		Leer nota;
		Segun nota Hacer
			1,2,3,4: Escribir "Suspenso";
			5: Escribir "Suficiente";
			6,7: Escribir "Bien";
			8: Escribir "Notable";
			9,10: Escribir "Sobresaliente";
			De Otro Modo:
				Escribir "Nota incorrecta";
		FinSegun
		Escribir "Programa terminado";
	FinProceso

En python3 utilizamos la alternativa múltiple:

	nota = int(input("Dime tu nota:"))
	if nota >=1 and nota <= 4:
        print("Suspenso")
    elif nota == 5:
        print("Suficiente")
    elif nota == 6 or nota == 7:
		print("Bien")
    elif nota == 8:
		print("Notable")
    elif nota ==9 or nota == 10:
		print("Sobresaliente")
    else:
		print("Nota incorrecta")
	print("Programa terminado")

