"""Ejercicio N°2
Programa que dado un rango de números enteros, obtiene la cantidad de números que contiene"""

print("-----------------------------------------")
print("---------- CANTIDAD DE NÚMEROS ----------")
print("-----------------------------------------")

c=0

# input 
print("Ingrese el primer número del rango:")
ni=int(input())
print(("Ingrese el último número del rango: "))
nf=int(input())

i=ni+1
# processing
while i<nf:
    i=i+1
    c=c+1 
    print(ni+c)
   

# output
print("La cantidad de números es: " +str(c))
