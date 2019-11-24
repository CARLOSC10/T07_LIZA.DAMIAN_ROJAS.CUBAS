#REPETITIVAS MIENTRAS QUE CALCULA SI UNA PERSONA INGRESA A LA UNPRG
import os
alumno,puntos_area,puntos_biomedicas,puntos_humanidades="",0,0,0

#ARGUMENTOS
alumno=os.sys.argv[1]
puntos_area=float(os.sys.argv[2])
puntos_biomedicas=float(os.sys.argv[3])
puntos_humanidades=float(os.sys.argv[4])

#PROCESSING
resultados_invalidos=(puntos_area<=31.5 or puntos_biomedicas<=0 or puntos_humanidades<=-1)

#WHILE
#MIENTRAS LOS DATOS SEAN INVALIDOS A LA CONDICION ENTRA EN EL WHILE
while(resultados_invalidos==True):
    print("RESULTADOS INVALIDOS:Ingrese nuevamente los datos")
    alumno=input("NOMBRE DEL POSTULANTE:")
    puntos_area=float(input("INGRESE PUNTOS DE AREA:"))
    puntos_biomedicas=float(input("INGRESE PUNTOS DE BIOMEDICAS:"))
    puntos_humanidades=float(input("INGRESE PUNTOS DE HUMANIDADES:"))
    resultados_invalidos=(puntos_area<=31.5 or puntos_biomedicas<=0 or puntos_humanidades<=-1)
#fin_while
print("FIN DEL BUCLE")
resultados=puntos_area+puntos_biomedicas+puntos_humanidades

#OUTPUT
print("")
print("#############################################")
print("              INGRESO A LA UNPRG             ")
print("#############################################")
print("ALUMNO:               ",alumno,"             ")
print("PUNTOS DE AREA:       ",puntos_area,"        ")
print("PUNTOS DE BIOMEDICAS: ",puntos_biomedicas,"  ")
print("PUNTOS DE HUMANIDADES:",puntos_humanidades," ")
print("RESULTADOS DE EXAMEN: ",resultados,"         ")
print("#############################################")
