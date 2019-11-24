import os
#mostrar la cantidad de numeros positivos ingresados si el usuario ingresa un numero negativo mostrar la cantidad de numeros positivos
#declaracion de variables
numero,cantidad_numeros_positivos=0,0

#input
numero=int(os.sys.argv[1])
if(numero>=0):
    cantidad_numeros_positivos+=1
#prossecing
#mientras el numero sea mayor o igual a cero pedir otro numero positivo
while(numero>=0):
    numero=int(input("ingrese otro numero positivo:"))
    cantidad_numeros_positivos +=1
#fin_while

cantidad_numeros_positivos=cantidad_numeros_positivos-1    #se asigna a la varriable cantidad numeros positivos ,la cantidad de numeros positivos menos 1
#output
print("LA CANTIDAD D NUMEROS POSITIVOS ES:",cantidad_numeros_positivos)
print("FIN DEL PROGRAMA")
