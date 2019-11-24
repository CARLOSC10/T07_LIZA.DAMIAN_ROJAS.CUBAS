import os
#contar la cantida de puntos en un texto ingresado
#declaracion de variables
cantidad_puntos,texto,texto_invalido=0,"",False

#input
texto=os.sys.argv[1]

#prossecing
#iterar:
for letra in texto:
    texto_invalido=(letra=="1" or letra=="2" or letra=="3" or letra=="4" or letra=="5" or letra=="6" or letra=="7" or letra=="8" or letra=="9" or letra=="10")
    while(texto_invalido):
        print("INGRESE OTRO TEXTO CORRECTA PARA DELETREAR")
        texto=input("ingrese palabra:")
        for letra in texto:
            texto_invalido=(letra=="1" or letra=="2" or letra=="3" or letra=="4" or letra=="5" or letra=="6" or letra=="7" or letra=="8" or letra=="9" or letra=="10")   #fin_while
    #fin_while
#fin_for

#fin_for
#iterar
for letra in texto:
    if (letra=="."):
        cantidad_puntos+=1
#fin_for
#output
print("*************************************************")
print("LA CANTIDAD DE PUNTOS ES:",cantidad_puntos)
print("*************************************************")
print("FIN DEL PROGRAMA")
