#Desafio 2 - Velocidad de Escape 

#Importación de librerias
import math

#Ingreso de variables, solicitar a ususario:
radio= float(input("Ingresar el radio del planeta en Km: "))
constante= float(input("Ingresar constante gravitacional en [m/s^2]: "))

#Convertir de Kilometros a metros
radio *=1000 # EL *= es una forma simple de multiplicar

#Formula 2, aplicar raiz cuadrada
velocidad_escape=round(math.sqrt(2*radio*constante),1)

#Imprimir resultado
print(f"\nLa velocidad de Escape es {velocidad_escape} [m/s] \n")





