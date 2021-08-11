"""#EJERCICIO18
palabra = input("Ingrese palabra: ")
for letra in palabra [::-1]:
    print(letra)"""

"""#EJERCICIO19
frase = input("Ingrese frase: ")
letra = input("Ingrese letra:")
cont = 0
for caracter in frase:
    if caracter == letra:
         cont += 1
print(f"La frase {frase} contiene {cont} veces la letra {letra}")"""

"""frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")
cont = frase.count(letra)

print(f"La frase contiene la letra {letra} {cont} veces")"""

"""#EJERCICIO20
ingrese=input("Ingrese palabra:")
while ingrese != "salir":
    print (ingrese)
    ingrese = input("Ingrese palabra:")"""
"""
#EJERCICIO21
asignaturas = ["Matematica", "Quimica", "Historia", "Filosofia"]
for asignatura in asignaturas:
    print(f"Yo estudio {asignatura}")"""

"""#EJERCICIO22
v_1= [1,2,3]
v_2 =[-1,0,2]
sum=0

for i in range(len(v_1)):
    elemento = v_1[i] * v_2[i]
    sum += elemento

print(sum)"""

"""#EJERCICIO23
list_precios={"Banana":80, "Manzana":100, "Pera":50, "Naranja":70}
fruta=input("Ingrese fruta o salir para salir: ").capitalize()
while fruta!="Salir":
    if fruta in list_precios:
        kilos= float(input("Ingrese cantidad de kilos: "))
        precio = kilos * list_precios [fruta]
        print (f"El precio total es {precio}")
    else:
        print("La fruta no existe")
    fruta = input("Ingrese fruta o salir para salir: ").capitalize()
"""
"""#EJERCICIO24
materias = {'Matematicas': 6, 'Fisica': 4, 'Quimica': 5}
cant_creditos = 0

for i, k in materias.items():
    print(f"{i} tiene {k} creditos")
    cant_creditos += k

print(f"El total de creditos es {cant_creditos}")
"""

"""#Ejercicio24
from string import ascii_lowercase
lista_abc = list (ascii_lowercase)
lista_2 = lista_abc.copy()
for letra in lista_2:
    if letra in "aeiou":
        lista_abc.remove(letra)
print (lista_abc)
print(lista_2)"""



