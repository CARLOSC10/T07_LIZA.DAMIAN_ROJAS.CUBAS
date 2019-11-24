#REPETITIVAS ITERACION RANGO QUE MUESTRA LOS N PRIMEROS NUMEROS, N SE ESCRIBE POR TECLADO
import os
n=0

#ARGUMENTO
n=int(os.sys.argv[1])

#INPUT QUE VALIDA DATOS
numero_invalido=(n<=0)

#WHILE
#MIENTRAS LOS DATOS SEAN INCORECTO A LA CONDICION ENTRA EN EL WHILE
while(numero_invalido==True):
    n=int(input("NUMERO INVALIDO:Ingrese nuevamente el numero:"))
    numero_invalido=(n<=0)
#fin_while
print("FIN DEL BUCLE")

#PROCESSING DE LA ESTRUCTURA "ITERACION RANGO"
for n in range(n):
    print(n)
#fin_iterar
