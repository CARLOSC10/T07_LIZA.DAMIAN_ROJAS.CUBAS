import os
#contar la cantidad de datos numericos y letras en una cadena de texto si se ingresa una cadena vacia("") pedir nuevamente el texto
#declaracion de variables
cantidad_numeros,cantidad_letras_espacios,texto,texto_invalido=0,0,"",False

#input
texto=os.sys.argv[1]

#prossecing
#verificador
texto_invalido=(texto=="")

#mientras el texto se invalido haver:
while(texto_invalido==True):
    print("TEXTO INVÁLIDO")
    texto=input("ingrese texto:")
    texto_invalido=(texto=="")
#fin_while
for caracter in texto:
    if (caracter=="0" or caracter=="1" or caracter=="2" or caracter=="3" or caracter=="4" or caracter=="5" or caracter=="6" or caracter=="7" or caracter=="8" or caracter=="9" ):
        cantidad_numeros+=1
    else:
        cantidad_letras_espacios+=1
#fin_for
#output
print("la cantidad de letras o espacios es:",cantidad_letras_espacios)
print("la cantidad de numeros es:",cantidad_numeros)
