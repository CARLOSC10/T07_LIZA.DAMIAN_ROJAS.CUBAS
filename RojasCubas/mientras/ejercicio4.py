import os
# distancia que a rrecorrido un auto que realizo(M.R.U.V)
print("")
#declaracion de variables
velocidad_inicial,tiempo,aceleracion,distancia,datos_invalidos,a=0.0,0.0,0.0,0.0,False,""

#input
velocidad_inicial=float(os.sys.argv[1])
tiempo=float(os.sys.argv[2])
aceleracion=float(os.sys.argv[3])

#processing
#validador del valor de los datos(velocidad_inicial,tiempo y aceleracion) del la distancia para poder calcularlo
datos_invalidos=((velocidad_inicial<0) or (tiempo<0) or (aceleracion<0))
#mientras los datos invalidos sea igual a verdadero mostrar un mensaje y pedir nuevamente los datos
while(datos_invalidos==True):
    print("DATOS INGRESADOS INVÁLIDOS,Ingrese valores correctos")
    velocidad_inicial=float(input("ingrese la velocidad_inicial:"))
    tiempo=float(input("ingrese el tiempo:"))
    aceleracion=float(input("ingrese la aceleracion:"))
    datos_invalidos=((velocidad_inicial<0) or (tiempo<0) or (aceleracion<0))
#fin_while
distancia=(velocidad_inicial*tiempo)+(aceleracion*tiempo**2)/2
#output
print("")
print("bucle concluido!")
print("DATOS VALIDOS")
print("calculando la Distancia...")

if(distancia==0.0):         #condicion:si la distancia es igual a cero mostrar el mensaje
    a="DISTANCIA CERO"    #asigna un valor en la variable a

elif(distancia>0.0 and distancia<150.0):     #condicion:si la distancia es mayor que cero y menor que 150 mostrar el mensaje
    a="DISTANCIA PEQUEÑA"                   #asigna un valor en la variable a

elif(distancia>150.0):      #condicion:si la distancia es mayor a 150 mostrar el mensaje
    a="DISTANCIA GRANDE"

#fin_if

print("************************************************************************")
print("*        DISTANCIA DE UN AUTO EN UN MOVIMIENTO(M.R.U.V)                *")
print("************************************************************************")
print("*la velocidad inicial es:",velocidad_inicial,"metros por segundo","                     *")
print("*el tiempo en segundos es:",tiempo,"                                       *")
print("*la aceleracion es:",aceleracion,"metros/segundo al cuadrado","                   *")
print("*la distancia que rrecorrió el auto es:",distancia,"metros","                 *")
print("************************************************************************")
print(a)
print("************************************************************************")
