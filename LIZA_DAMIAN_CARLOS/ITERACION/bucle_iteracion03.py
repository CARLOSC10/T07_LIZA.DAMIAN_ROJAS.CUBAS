#REPETITIVAS ITERACION QUE INPRIME LOS PRIMEROS NUMEROS PARES O IMPARES SEGUN EL NUMERO INGRESADO POR TECLADO
#SI EL NUMERO INGRESADO POR TECLADO ES PAR ENTONSES TE INPRIME LOS PRIMEROS NUMEROS PARES
#SI EL NUMERO INGRESADO POR TECLADO ES IMPAR ENTONSES TE IMPRIME LOS PRIMEROS NUMEROS IMPARES
import os

#ARGUMENTO
#ASIGNACION DE VALORES
valor=int(os.sys.argv[1])
numeros=(1,3,5,7,9,11,13,15,17,19,21)

#PROCESSING DE LA ESTRUCTURA "ITERACION"
for x in numeros:
    print(x*valor)
#fin_iterar
print("FIN DEL BUCLE")
