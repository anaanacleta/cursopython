import math
class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def cuadrante(self):
        if self.x ==0 and self.y !=0:
            print("Se situa sobre eje Y")
        if self.x!=0 and self.y ==0:
            print ("Se situa sobre eje X")
        if self.x ==0 and self.y ==0:
            print("Se situa sobre origen")
        if self.x > 0 and self.y >0:
            print("Se situa sobre cuadrante 1")
        if self.x > 0 and self.y < 0:
                print("Se situa sobre cuadrante 4")
        if self.x < 0 and self.y >0:
            print(f"{self}Se situa sobre cuadrante 2")
        if self.x < 0 and self.y < 0:
            print(f"{self}Se situa sobre cuadrante 3")

    def vector(self,p):
        v_res_x, v_res_y = p.x - self.x, p.y - self.y
        print(f"({v_res_x}, {v_res_y})")

    def distancia(self, p):
            v_res_x, v_res_y = p.x - self.x, p.y - self.y
            d = math.sqrt(v_res_x ** 2 + pow(v_res_y, 2))
            print(f"{d:.2f}")
            # return d



punto_1 = Punto(0, 1)
punto_2=Punto (4,5)
punto_3 = Punto (-2, -6)
punto_4 = Punto (-4, 6)
punto_5 = Punto(4, -8)
"""punto_1.cuadrante()
punto_2.cuadrante()
punto_3.cuadrante()
punto_4.cuadrante()
punto_5.cuadrante()
punto_5.vector(punto_2)"""

class Rectangulo:
    def __init__(self, pinicial=Punto(), pfinal=Punto()):
        self.pinicial = pinicial
        self.pfinal = pfinal

    def base(self):
        b = abs(self.pfinal.x - self.pinicial.x)
        return b

    def altura(self):
        a = abs(self.pfinal.y - self.pinicial.y)
        return a

    def area(self):
        ar = self.base() * self.altura()
        return ar

A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto()

r = Rectangulo(A, B)
print(r.base())
print(r.altura())
print(r.area())
