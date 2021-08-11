#EJERCICIO1
class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def mostrar1(self):
        print(f"Nombre: {self.nombre}\n Edad: {self.edad}\n DNI:{self.dni}")

    def EsMayorDeEdad(self):
        if self.edad >= 18:
            return True
        else:
             return False

#Ejercicio2
class Cuenta:
    def __init__(self, titular =Persona (), cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad


    def ingresar (self, x):
        if x < 0:
            pass
        else:
            self.cantidad += x

    def retirar (self, x):
        self.cantidad -= x


    def mostrar(self):
        print("Datos de la cuenta")
        print(self.titular.mostrar())
        print(f"Cantidad --> {self.cantidad}")



class CuentaJoven (Cuenta):
    def __init__(self, titular, cantidad, bonificacion):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    def TitularValido (self):
        if self.titular.EsMayorDeEdad() and self.titular.edad < 25:
            return True
        else:
            return False

    def retirar (self, x):
        if self.TitularValido():
            self.cantidad -= x

    def mostrar (self):
        if self.TitularValido():
            print(f"CuentaJoven Cantidad: {self.cantidad} y bonificacion: {self.bonificacion}")

    def CumplirAños(self, x):
        self.titular.edad += x


Annick =Persona ("Annick", 28, 37216969)
Lara =Persona("Lara", 15, 45286932)
Sol =Persona ("Sol", 22, 39215469)

Annick_Cuenta= Cuenta(Annick, 100)
Lara_Cuenta = Cuenta(Lara,500)
Sol_Cuenta = Cuenta(Sol, 1000)
Annick_Cuenta.ingresar(200)
Annick_Cuenta.ingresar (-100)
Annick_Cuenta.retirar(50)
Lara_Cuenta.ingresar(50)
Lara_Cuenta.retirar(100)


Cuenta_1 = CuentaJoven (Annick, 200, 20)
Cuenta_1.TitularValido()
Cuenta_1.mostrar()

Cuenta_2= CuentaJoven (Sol_Cuenta.titular, Sol_Cuenta.cantidad, 10)
Cuenta_2.mostrar()
Cuenta_2.retirar(100)
Cuenta_2.mostrar()
Cuenta_2.ingresar(400)
Cuenta_2.mostrar()
Cuenta_2.titular.mostrar1()
Cuenta_2.CumplirAños(5)
Cuenta_2.titular.mostrar1()
Cuenta_2.retirar (200)
Cuenta_2.titular.mostrar()