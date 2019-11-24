#REPETITIVAS ITERACION RANGO QUE INPRIME UNA CALCULADORA DE CUALQUIER NUMERO DADO POR TECLADO
import os

#ARGUMENTO
#ASIGNACION DE VALORES
valor=int(os.sys.argv[1])

#PROCESSING DE ESTRUCTURA "ITERACION RANGO"
for numero in range(0,13):
    print(valor, "x", numero,"=",valor*numero)
#fin_iterar
print("FIN DEL BUCLE")
