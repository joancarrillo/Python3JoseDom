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
# Programa principal
punto1=punto3d()
punto2=punto(4,5,3)
print(punto1.distancia(punto2))
