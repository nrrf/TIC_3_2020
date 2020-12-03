class Persona():
    def __init__(self,nombre,edad,cedula,genero):
        self.nombre = str(nombre)
        self.edad = int(edad)
        self.cedula = int(cedula)
        self.genero = str(genero)
    def saludar(self):
        print("el nombre: {}, tiene edad {}, cedula {}, y genero{}".format(self.nombre,self.edad,self.cedula,self.genero))
lista = []
opcion = 1
while(True):
 opcion = int(input("Ingrese Opcion "))
 if opcion==1:
   nombre = input("Ingrese nombre ")
   edad = int(input("Ingrese edad "))
   cc = int(input("Ingrese la cedula "))
   genero = input("Ingrese genero ")
   Personn = Persona(nombre,edad,cc,genero)
   lista.append(Personn)
 elif opcion == 2:
   for i in lista:
     print(i.nombre)
 else:
   print("Salida del programa")
   break




