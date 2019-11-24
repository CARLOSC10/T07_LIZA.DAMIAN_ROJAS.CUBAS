#REPETITIVAS MIENTRAS QUE CALCULA EL AREA DE TRAPECIO
import os
Base_mayor,Base_menor,altura=0,0,0

#ARGUMENTOS
Base_mayor=int(os.sys.argv[1])
Base_menor=int(os.sys.argv[2])
altura=int(os.sys.argv[3])

#PROCESSING
area_invalidad=(Base_mayor<=1 or Base_menor<=5 or altura<=0)

#WHILE
#MIENTRAS LOS DATOS DEL AREA DEL TRAPECIO SEAN INCORECTOS A LA CONDICION ENTRA EN EL WHILE
while(area_invalidad==True):
    print("DATOS INGRESADOS INVALIDOS:Ingrese nuevamente los datos:")
    Base_mayor=int(input("INGRESE LA BASE MAYOR:"))
    Base_menor=int(input("INGRESE LA BASE MENOR:"))
    altura=int(input("INGRESE LA ALTURA DEL TRAPECIO:"))
    area_invalidad=(Base_mayor<=1 or Base_menor<=5 or altura<=0)
#fin_while
print("FIN DEL BUCLE")
area_trapecio=((Base_mayor+Base_menor)/2*altura)


#OUTPUT
print("##########################################")
print("#           AREA DEL TRAPECIO            #")
print("##########################################")
print("# BASE MAYOR:    ",Base_mayor,"           ")
print("# BASE MENOR:    ",Base_menor,"           ")
print("# ALTURA:        ",altura,"               ")
print("# AREA TRAPECIO: ",area_trapecio,"        ")
print("##########################################")
