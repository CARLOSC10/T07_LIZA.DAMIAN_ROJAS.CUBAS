#REPETITIVAS "PARA" QUE MUESTRA LA SUMA DE LOS N NUMEROS, N SE ESCRIBE POR TECLADO
import os
numero=0

#ARGUMENTOS
numero=int(os.sys.argv[1])

#INPUT QUE VALIDA DATOS
datos_incorrectos=(numero<0)

#WHILE
#MIENTRAS LOS DATOS SEAN INCORECTO A LA CONDICION ENTRA EN EL WHILE
while(datos_incorrectos==True):
    numero=int(input("NUMERO INVALIDO:Ingrese nuevamente el numero:"))
    datos_incorrectos=(numero<0)
#fin_while
print("FIN DEL BUCLE")

#PROCESSING DE LA ESTRUCTURA "PARA"
i=0
suma=0
while(i<=numero):
    suma += i
    i += 1
#fin_while
print("SUMA DEl N NUMERO ESCRITO POR TECLADO ES:",suma)


