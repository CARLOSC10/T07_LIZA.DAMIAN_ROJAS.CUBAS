import os
#mostrar la cantidad de numeros impares desde cero hasta el numero indicado por el usuario
#declaracion de variables
numero_limite,numero_inavalido,contador_impares,i=0,False,0,0

#input
numero_limite=int(os.sys.argv[1])

#prossecing
#verificador
numero_inavalido=(numero_limite<0)
#mientras el numero invalido sea verdadero pedir nuevamente el numero
while(numero_inavalido==True):
    print("NUMERO INVÁLIDO")
    numero_limite=int(input("ingrese un numero limite mayor o igual a cero:"))
    numero_inavalido=(numero_limite<0)
#fin_while
i=0
contador_impares=0
#mientras i sea menor que el numero limite hacer:
while(i<numero_limite):
    i+=1
    if(i%2==1):
        contador_impares=contador_impares+1
#fin_while
print("LA CANTIAD DE NUMEROS IMPARES COMPRENDIDOS ENTRE :0 Y "+str(numero_limite)+" ,Es: "+str(contador_impares))

