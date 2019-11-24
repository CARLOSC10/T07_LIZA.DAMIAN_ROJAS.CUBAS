#REPETITIVAS MIENTRAS QUE CALCULA LAS NOTAS DE MATEMATICA II
import os
nota_uno,nota_dos,nota_tres,nota_cuatro=0,0,0,0

#ARGUMENTOS
nota_uno=int(os.sys.argv[1])
nota_dos=int(os.sys.argv[2])
nota_tres=int(os.sys.argv[3])
nota_cuatro=int(os.sys.argv[4])

#PROCESSING
notas_invalidad=(nota_uno<=0 or nota_dos<=0 or nota_tres<=0 or nota_cuatro<=0)

#WHILE
#MIENTRAS LAS NOTAS SEAN INCORECTOS ENTRAN EN EL WHILE
while(notas_invalidad==True):
    print("DATOS INGRESADOS INVALIDOS:Ingrese nuevamente los datos")
    nota_uno=int(input("INGRESE LA NOTA 01:"))
    nota_dos=int(input("INGRESE LA NOTA 02:"))
    nota_tres=int(input("INGRESE LA NOTA 03:"))
    nota_cuatro=int(input("INGRESE LA NOTA 04:"))
    notas_invalidad=(nota_uno<=0 or nota_dos<=0 or nota_tres<=0 or nota_cuatro<=0)
#fin_while
print("FIN DEL BUCLE")
notas_totales=(nota_uno+nota_dos+nota_tres+nota_cuatro)/4

#OUTPUT
print("")
print("###################################")
print("      NOTAS DE MATEMATICA II       ")
print("###################################")
print("# NOTA 01: ",nota_uno,"            ")
print("# NOTA 02: ",nota_dos,"            ")
print("# NOTA 03: ",nota_tres,"           ")
print("# NOTA 04: ",nota_cuatro,"         ")
print("# NOTAS TOTAL:",notas_totales,"    ")
print("###################################")


