import os
#mostrar la cantidad de números ingresados por teclado(desde el cero)
#declaracion de variables
cantidad_numero,i,numero_invalido=0,0,False

#input
cantidad_numero=int(os.sys.argv[1])

#prossecing
#verificador
numero_invalido=(cantidad_numero<0)
i=0

#mientras la cantidad de numero sea invalida pedirlo nuevamente
while(numero_invalido==True):
    print("CANTIDAD DE NUMERO INCORRECTO")
    cantidad_numero=int(input("ingrese numero:"))
    numero_invalido=(cantidad_numero<0)
#fin_while

#mientras i se menor igual  a cantidad_numero hacer:
while(i<=cantidad_numero):
    print(i)
    i+=1
#fin_while

#output
print("FIN DEL PROGRAMA")
