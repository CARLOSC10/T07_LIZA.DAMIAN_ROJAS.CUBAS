#REPETITIVAS "PARA" QUE MUESTRA LOS 60 PRIMEROS NUMEROS Y SI LE PONES UN NUMERO <=-1 O >=61
#TE PEDIRA INGRESE EL NUMERO CORRECTO QUE ESTA DESDE >=0 HASTA <=60
import os
numero=0

#ARGUMENTOS
numero=int(os.sys.argv[1])

#INPUT QUE VALIDA DATOS
numero_invalido=(numero<=-1 or numero >=61)

#WHILE
while(numero_invalido==True):
    numero=int(input("NUMERO INCORECTO SU NUMERO ES >=61 O <=-1:Ingrese el numero correcto que es >=0 O <=60:"))
    numero_invalido=(numero<=-1 or numero >=61)
#fin_while
print("FIN DEL BUCLE")

#PROCESSING DE LA ESTRUCTURA "PARA"
i=10
while(i<=60):
    print(i)
    i +=1
#fin_de_whilw
