import os
#mostrs cada letra de una palabra ingresada
##declaracion de variables
palabra,palabra_invalida="",False
#input
palabra=os.sys.argv[1]

#prossecing
#verificar que no sea un numero
for letra in palabra:
    palabra_invalida=(letra=="1" or letra=="2" or letra=="3" or letra=="4" or letra=="5" or letra=="6" or letra=="7" or letra=="8" or letra=="9" or letra=="10")
    while(palabra_invalida):
        print("INGRESE OTRA PALABRA CORRECTA PARA DELETREAR")
        palabra=input("ingrese palabra:")
        palabra_invalida=(letra=="1" or letra=="2" or letra=="3" or letra=="4" or letra=="5" or letra=="6" or letra=="7" or letra=="8" or letra=="9" or letra=="10")
        for letra in palabra:
            palabra_invalida=(letra=="1" or letra=="2" or letra=="3" or letra=="4" or letra=="5" or letra=="6" or letra=="7" or letra=="8" or letra=="9" or letra=="10")
    #fin_while
#fin_for
for letra in palabra:
        print(letra)
#output
print("****************")
print("FIN DEL PROGRAMA")



