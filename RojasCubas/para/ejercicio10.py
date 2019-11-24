import os
#algoritmo para sumar solo numeros pares(positivos o negativos) y numeros impares(positivos o negativos) comprendidos  entre ciertos numeros (difente de cero) indicados por el usuario
#declaracion de variables
numero_inicial,numero_final,datos_invalidos,suma_numeros_par,suma_numeros_impar=0,0,False,0,0

#input
numero_inicial=int(os.sys.argv[1])
numero_final=int(os.sys.argv[2])

#prosecing
#verificador
datos_invalidos=(numero_inicial==0 or numero_final==0 or numero_inicial>numero_final)

#mentras las datos invalidos sean igaual a verdadero ,hacer:
while(datos_invalidos==True):
    print("DATO INGRESADO ERRÓNEO,INGRESE NUEVAMENTE LOS DATOS(DIFEREBTE DE CERO Y NUMERO INICIAL NO PUEDE SER MAYOR A NUMERO FINAL)")
    numero_inicial=int(input("ingrese numero inicial:"))
    numero_final=int(input("ingrese numero final:"))
    datos_invalidos=(numero_inicial==0 or numero_final)
#fin_while
#mientras numero inicial sea menor a numero final hacer:
while(numero_inicial<numero_final):
    numero_inicial +=1
    if(numero_inicial%2==0):
        suma_numeros_par=suma_numeros_par+numero_inicial

    else:
        suma_numeros_impar=suma_numeros_impar+numero_inicial
    #fin_if
#fin_while
print("FIN DE LOS BUCLES!")
#output
print("*****************************************************")
print("LA SUMA DE NUMEROS PARES ES:",suma_numeros_par)
print("LA SUMA DE NUMEROS IMPARES ES:",suma_numeros_impar)
print("*****************************************************")
print("FIN DEL PROGRAMA")
