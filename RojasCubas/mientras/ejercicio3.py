import os
#Área del trapecio(en metros cuadrados)
#declararación de variables
base_menor,base_mayor,altura,area_trapecio,datos_invalidos,a=0.0,0.0,0.0,0.0,False,""

#input
base_menor=float(os.sys.argv[1])
base_mayor=float(os.sys.argv[2])
altura=float(os.sys.argv[3])

#processing
#verificador de elementos del area para poder calcularlo
datos_invalidos=(base_menor<=0 or base_mayor<=0 or altura<=0)

#mientras los datos_invalidos se verdadero mostrar un mensaje y pedir nuevamente los elementos del area
while(datos_invalidos==True):
    print("DATO INGRESADO INVALIDO!,Ingrese nuevamente los Datos")
    base_menor=float(input("ingrese base menor:"))
    base_mayor=float(input("ingrese base mayor:"))
    altura=float(input("ingrese altura:"))
    datos_invalidos=(base_menor<=0 or base_mayor<=0 or altura<=0)
#fin_while
area_trapecio=((base_mayor+base_menor)/2)*altura

#output
print("")
print("bucle terminado!")
print("DATOS VALIDOS")
print("calculando el Area del Trapecio...")

#condicion si el area es mayor a 500.0 mostrar area extensa sino mostrar area pequeña
if(area_trapecio>500.0):
    a="ÁREA EXTENSA"         #asigna un mensaje en la variable a

else:
    a="ÁREA PEQUEÑA"       #asigna un mensaje en la variable a

print("**************************************************")
print("*                ÁREA DEL TRPECIO                *")
print("**************************************************")
print("*la base menor:",base_menor,"m")
print("*la Base mayor:",base_mayor,"m")
print("*la altura:",altura,"m")
print("*el area del Trapecio:",area_trapecio,"metros cuadrados")
print("**************************************************")
print(a)
print("**************************************************")
