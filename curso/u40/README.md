# Polimorfismo, herencia y delegación
	
## Polimorfismo

El polimorfismo es la técnica que nos posibilita que al invocar un determinado método de un objeto, podrán obtenerse distintos resultados según la clase del objeto. Esto se debe a que distintos objetos pueden tener un método con un mismo nombre, pero que realice distintas operaciones.

Esto es posible debido a que python es dinámico, es decir en tiempo de ejecución es cuando se determina el tipo de un objeto. Veamos un ejemplo:

	class gato():
		def hablar(self):
			print("MIAU")	

	class perro():
		def hablar(self):
			print("GUAU")	

	def escucharMascota(animal):
		animal.hablar()	

	g = gato()
	p = perro()
	escucharMascota(g)
	escucharMascota(p)

## Herencia

La herencia es un mecanismo de la programación orientada a objetos que sirve para crear clases nuevas a partir de clases preexistentes. Se toman (heredan) atributos y métodos de las clases viejas y se los modifica para modelar una nueva situación.

La clase desde la que se hereda se llama clase base y la que se construye a partir de ella es una clase derivada.

Si nuestra clase base es la clase `punto` estudiadas en unidades anteriores, puedo crear una nueva clase de la siguiente manera:

	class punto3d(punto):
		def __init__(self,x=0,y=0,z=0):
			super().__init__(x,y)
			self.z=z
        
        def mostrar(self):
            return super().mostrar()+":"+str(self.z)

		def distancia(self,otro):
			dx = self.x - otro.x
			dy = self.y - otro.y
			dz = self.z - otro.z
			return (dx*dx + dy*dy + dz*dz)**0.5	

Creemos dos objetos de cada clase y veamos los atributos y métodos que tienen definido:

	>>> p=punto(1,2)
	>>> p3d=punto3d(1,2,3)

## La función super()

La función `super()` me proporciona una referencia a la clase base. Y podemos observar que hemos reescrito el método `distancia` y `mostrar`:

	>>> p.distancia(punto(5,6))
	5.656854249492381
	>>> p3d.distancia(punto3d(2,3,4))
	1.7320508075688772

## Delegación

Llamamos delegación a la situación en la que una clase contiene (como atributos) una o más instancias de otra clase, a las que delegará parte de sus funcionalidades.

A partir de la clase `punto`, podemos crear la clase `circulo` de esta forma:

	class circulo():	

		def __init__(self,centro,radio):
			self.centro=centro
			self.radio=radio	

		def mostrar(self):
			return "Centro:{0}-Radio:{1}".format(self.centro.mostrar(),self.radio)	

Y creamos un objeto `circulo`:

	>>> c1=circulo(punto(2,3),5)
	>>> print(c1.mostrar())
	Centro:2:3-Radio:5
