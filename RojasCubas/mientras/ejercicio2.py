import os
#acceder a una cuenta con nombre,usuario("12345F") y contraseña("1234567")
print("")
#declararación de variables
nombre,usuario,contraseña,datos_invalidos,a="","","",False,""

#input
nombre=os.sys.argv[1]
usuario=os.sys.argv[2]
contraseña=os.sys.argv[3]

#processing
#verificador de usuario y contraseña
datos_invalidos=(usuario!="12345F" and contraseña!="1234567")

#mientras los datos_invalidos sea verdadero mostrar un mensaje y pedir nuevamente el usuario y contraseña
while(datos_invalidos==True):
    print("EL USUARIO O CONTRASEÑA ES INVALIDO INGRESE NUAVEMENTE LOS DATOS ")
    usuario=input("ingrese usuario:")
    contraseña=input("ingrese contraseña:")
    datos_invalidos=(usuario!="12345F" and contraseña!="1234567")
#fin_while
#output
print("")
print("bucle concluido!")
print("USUARIO y CONTRASEÑA VAIIDOS")
print("mostrando los Datos de la Cuenta...")


print("**************************************")
print("*             CUENTA                 *")
print("**************************************")
print("*NOMBRE:",nombre)
print("*USUARIO:",usuario)
print("*CONTRASEÑA:",contraseña)
print("**************************************")
print("ACCESO PERMITIDO")
print("**************************************")
