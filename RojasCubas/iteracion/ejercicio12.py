import os
#verificar contar el número de digitos del DNI de un usuario
#declaracion de variables
cantidad_digitos,nro_dni_invalido,nro_dni=0,False,0

#input
nro_dni=os.sys.argv[1]
#prossecing
#verificador
nro_dni_invalido=((len(str(nro_dni_invalido))!=8))

#mientras el nro de dni sea inavalido pedir nuevamente el nro:
while(nro_dni_invalido==True):
    print("NUMERO DE DNI INVÁLIDO ")
    nro_dni=input("ingrese nro dni:")
    nro_dni_invalido=(len(str(nro_dni))!=8)
#fin_while
#iterarcion :
for digito in nro_dni:
    cantidad_digitos+=1
#fin_for

#output
print("la cantidad de digitos es:",cantidad_digitos)

