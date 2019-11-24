import os
#mostra los numeros desde -5 hasta 5
#declaracion de variables
numero1,numero2,numero_invalido=0,0,False
#input
numero1=int(os.sys.argv[1])
numero2=int(os.sys.argv[2])
#verificador1
numero_invalido=(numero1!=-5 or numero2!=5)
while(numero_invalido==True):
    print("NUMERO INCORRECTO,ingrese numero1=-5 y numero2=5")
    numero1=int(input("ingrese numero1:"))
    numero2=int(input("ingrese numero2:"))
    numero_invalido=(numero1!=-5 or numero2!=5)
#fin_whuile
#iterar en rango
for i in range(numero1,numero2):
    print(i)
#fin_for_in_range
print("FIN")
