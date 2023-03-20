class Persona:
    
    def __init__(self, nombre="", edad=0,dni=0):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    @property
    def gs_nombre(self):
         return self.nombre
    @ gs_nombre.setter
    def gs_nombre(self,xno):
        if len(xno) < 5:
           raise ValueError("No se pueden ingresar nombres vacios o cortitos!") 
        self.nombre=xno

    @property
    def get_edad(self):
         return self.edad
    @ get_edad.setter
    def get_edad(self,x):
        if x < 18:
           raise ValueError("Solo mayores!!!") 
        self.edad=x
    # Métodos de clase
    def mostrar(self):
        print("Hola, mi nombre es", self.nombre)
        print("Mi Dni es",self.dni)
        print("Tengo",self.edad,"Años")

    def es_mayor_de_edad(self):
        if self.edad > 17:
            ade = "Mayor"
        else:
            ade= "Menor"
        return(ade)

class Cuenta:
    def __init__(self,titular,cantidad=0):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        print(self.titular,self.cantidad)    
        
    def ingresar(self,xcantidad):
        if xcantidad <= 0:
           print("Importe invalido, la operacion no se realiza")  
        else:   
           nuevo_saldo=self.cantidad+xcantidad
           self.cantidad=nuevo_saldo

    def retirar(self,xcantidad):
        if xcantidad <= 0:
           print("Importe invalido, la operacion no se realiza")  
        else:   
           nuevo_saldo=self.cantidad-xcantidad
           self.cantidad=nuevo_saldo


class CuentaJoven(Cuenta):
    def __init__(self,titular,cantidad,bonif=25):
         Cuenta.__init__(self,titular,cantidad)
         self.bonif= bonif

    def __str__(self):
        cadena= "'\n\n\nCUENTA JOVEN  \n"
        cadena += f"{self.titular}    - Titular \n"
        cadena += f"{self.cantidad}  - Saldo \n"
        cadena += f"{self.bonif}     -% de Bonificacion \n"
 
        return cadena
    
    def mostrar(self):
        print(self)
    
    def Titular_Valido(self,persona):
        wedad= persona.edad
        wada= wedad >= 18 and wedad <= 25
        return wada

    def retirar(self,xcantidad,persona):
        if xcantidad <= 0:
           print("Importe invalido, la operacion no se realiza")  
           return
        if not self.Titular_Valido(persona):
            print("Edad invalida!!!!")            
        else:
            print("Tobo bien con la edad!")
            nuevo_saldo=self.cantidad-xcantidad
            self.cantidad=nuevo_saldo
    

# pruebas para el codigo
persona1 = Persona("Sergio",57,18139230)       
persona1.mostrar()
aco=persona1.nombre
print(aco)
persona1.gs_nombre="Manuel"
persona1.mostrar()
persona1.get_edad=44
persona1.mostrar()

cliente1=Cuenta(persona1.nombre,1000)
cliente1.mostrar()
cliente1.ingresar(800)
cliente1.mostrar()
cliente1.retirar(400)
cliente1.mostrar()
persona2=Persona("Alberto",20,323232)
cliente2=Cuenta(persona2.nombre,6000.78) 
cliente2.retirar(2000.44)
cliente2.mostrar()
cliente2.cantidad=5555
cliente2.mostrar()

persona3=Persona("Maria",24,454545)
persona3.mostrar
print(persona3.get_edad)
cuenta3=CuentaJoven(persona3.nombre,54000,33)
cuenta3.mostrar()
cuenta3.retirar(5000,persona3)    
cuenta3.mostrar()
