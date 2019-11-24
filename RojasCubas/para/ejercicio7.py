import  os
#suma de los 20 numeros siguientes a paartir del numero 20
#declaracion de variables
numero,numero_invalido,i,suma=0,False,0,0

#input
numero=int(os.sys.argv[1])

#prossecing
#verifcador
numero_invalido=(numero<=20)
#mientras el numero sea verdadero pedir nuevamnete el numero
while(numero_invalido==True):
    print("NUMERO INCORRECTO")
    numero=int(input("ingrese el numero mayor que 20:"))
    numero_invalido=(numero<=20)
#fin_while

#mientras numero sea menor que 41 hacer:
while(numero<41):
    numero+=1
    suma=suma+i
#fin_while

#output
print("LA SUMA ES:",suma)
print("FIN DEL PROGRAMA")
