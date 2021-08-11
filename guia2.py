"""def rectangulo (caracter="1"):
    anchura = int(input("Ingrese anchura:"))
    altura = int(input("Ingrese altura:"))
    for i in range(altura):
        print(anchura * caracter)

rectangulo ()"""
"""
def rectangulo ():
    anchura = int(input("Ingrese anchura:"))
    altura = int(input("Ingrese altura:"))
    caracter = input("Ingrese caracter:")
    for i in range(altura):
        print(anchura * caracter)

rectangulo ()"""

"""#CONTADORANIOSBISIESTOS
anio1 =int(input("Ingrese año: "))
anio2=int(input(f"Escriba otro año posterior a {anio1}: "))
if anio2 <= anio1:
        anio2 =int(input(f"{anio2} no es posterior a {anio1}Intentelo de nuevo: "))
cant_anios= (anio2 - anio1)
cont= 0
lis=[]
for i in range(anio1, anio2 + 1):
       if i % 4 == 0 and i % 100 != 0:
               cont+=1
               lis.append(i)
       elif i % 400 == 0:
                cont += 1
                lis.append(i)

print(f"De {anio1} a {anio2} hay {cant_anios} años. {cont} de ellos son bisiestos")
print(f"Estos son {lis}")"""

#Ejercicio7
def generador_de_listas():
    cantidad_listas= int(input("Digame cuantas listas quiere crear: "))
    listas_final = []
    for lista in range (1, cantidad_listas +1):
        cant_palabras= int(input(f"Digame cuantas palabras tiene la lista {lista}:"))
        list_palabras=[]
        for palabra in range(1, cant_palabras+1):
            palabras=input(f"Ingrese palabra {palabra}: ")
            list_palabras.append(palabras)
        listas_final.append((f"lista #{lista}", list_palabras))
    for i, k in listas_final:
        print(k,i)

generador_de_listas()

"""#EJERCICIO8
def num_comparar (a,b):
    if a > b:
        print("Mayor")
    if a < b:
        print("Menor")
    if a ==b:
        print ("Iguales")

num_comparar (152,234)
num_comparar (34,2)
num_comparar (300,300)"""

"""#EJERCICIO9
import random
def juego():
    numero= random.randint(0,1000)
    num_us= int(input("Ingrese numero: "))
    intentos = 1
    print(numero)

    while intentos < 7:
            if num_us > numero:
                print ("Es más bajo")
                num_us = int(input("Ingrese numero: "))
            if num_us < numero:
                print("Es más alto")
                num_us = int(input("Ingrese numero: "))
            if num_us == numero:
                print ("Viva Python")
                break
            intentos += 1
    else:
         print("BOO al piste perdiste")
juego()"""

"""def invertida (frase):
    frase= frase.split()
    frase_dada_vuelta = []
    for palabra in frase:
        pal_dada_vuelta = palabra [::-1]
        frase_dada_vuelta.append(pal_dada_vuelta)
    frase = " ".join(frase_dada_vuelta)
    print(frase)


invertida ("Esto es una prueba")
"""
"""
def dos_palabras (palabra1,palabra2):
     if len(palabra1) != len(palabra2):
        pal_mas_larga = max(len(palabra1), len(palabra2))
        palabra1 = palabra1.ljust(pal_mas_larga)
        palabra2 = palabra2.ljust(pal_mas_larga)

     for i, k in zip(palabra1, palabra2):
         print(i, k)


dos_palabras ("annick", "capa")"""

"""def tupla_ordenada(tupla):
    tupla_ord = list(tupla)
    tupla_ord.sort()
    tupla_ord = tuple(tupla_ord)
    if tupla == tupla_ord:
        print("Está ordenada de menor a mayor.")
    else:
        print("No está ordenada de menor a mayor")

tupla_ordenada((1,2,6,4,8))
tupla_ordenada((1,2,6,7,8))"""

"""def s_hm_s (segundos):
    mins, seg = divmod(segundos,60)
    hrs, mins = divmod (mins, 60)
    print (f"{hrs}hs {mins}min {seg} seg")

def hms2s (hrs, mins, segs):
    segundos = hrs*3600 + mins *60 + segs
    print(f"{segundos}seg")
s_hm_s (1000)
hms2s(0,16,40)"""
"""
def numeros():
    lista_num = []
    for i in range (3):
        num= int(input("Ingrerse un numero:"))
        lista_num.append (num)

    print(min(lista_num))
    print(max(lista_num))
    print(sum(lista_num)/len(lista_num))

numeros()"""

"""
def palabras(*pals):
    cant_letras = 0
    pal_mas_larga = ""
    for palabra in pals:
        cant_carac = len(palabra)
        if cant_carac > cant_letras:
            cant_letras = cant_carac
            pal_mas_larga = palabra
    print(f"La palabra más larga de la lista es {pal_mas_larga} y tiene {cant_letras} letras")


palabras("mesa", "silla", "ventana", "celular", "chocolate")"""
