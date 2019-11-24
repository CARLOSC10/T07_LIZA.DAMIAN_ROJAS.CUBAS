import os
#calcular la suma de cifras de un numero mayor que cero
#declaracion de variables
numero,numero_invalido,suma_cifras,cifra1,cifra2,cifra3,cifra4,cifra5,cifra6,cifra7,cifra8,cifra9,cifra10=0,True,0,0,0,0,0,0,0,0,0,0,0

#input
numero=int(os.sys.argv[1])

#prossecing
numero_invalido=(numero<0)

#mientras el numero invalido sea verdadero
while(numero_invalido==True):
    print("NÚMERO INVÁLIDO")
    numero=int(input("ingrese numero:"))
    numero_invalido=(numero<0)
#fin_while

#iteracion:
for cifra in str(numero):
    if (cifra=="0"):
        cifra1=0
    elif(cifra=="1"):
        cifra2=1
    elif(cifra=="2"):
        cifra3=2
    elif(cifra=="3"):
        cifra4=3
    elif(cifra=="4"):
        cifra5=4
    elif(cifra=="5"):
        cifra6=5
    elif(cifra=="6"):
        cifra7=6
    elif(cifra=="7"):
        cifra8=7
    elif(cifra=="8"):
        cifra9=8
    elif(cifra=="9"):
        cifra10=9
#fin_for
suma_cifras=cifra1+cifra2+cifra3+cifra4+cifra5+cifra6+cifra7+cifra8+cifra9+cifra10
#output
print("LA SUMA DE CIFRAS ES:",suma_cifras)
