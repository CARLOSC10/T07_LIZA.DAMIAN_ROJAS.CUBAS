#REPETITIVAS "PARA" QUE MUESTRA LOS N PRIMEROS NUMEROS, N SE ESCRIBE POR TECLADO
import os
n=0

#ARGUMENTOS
n=int(os.sys.argv[1])

#INPUT VALIDA LOS DATOS
datos_incorectos=(n<0)

#WHILE
#MIESTRAS LOS DATOS SEAN INCORECTOS A LA CONDICION ENTRA EN WHILE
while(datos_incorectos==True):
    n=int(input("DATOS INGRESADOS INVALIDOS:Ingrese nuevamente los datos:"))
    datos_incorectos=(n<0)
#fin_while
print("FIN DEL BUCLE")

#PROCESSING DE LA ESTRUCTURA "PARA"
i=0
while(i<=n):
    print(i)
    i+=1
#fin_while


