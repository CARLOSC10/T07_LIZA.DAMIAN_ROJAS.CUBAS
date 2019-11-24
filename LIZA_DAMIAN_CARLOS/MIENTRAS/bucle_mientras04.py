#REPETITIVAS MIENTRAS QUE CALCULA LA RESISTENCIA ELECTRICA
import os
resistencia_inicial,coeficiente_de_T,variacion_de_T=0.0,0.0,0.0

#ARGUMENTOS
resistencia_inicial=float(os.sys.argv[1])
coeficiente_de_T=float(os.sys.argv[2])
variacion_de_T=float(os.sys.argv[3])

#PROCESSING
resistencia_invalidad=(resistencia_inicial<=5 or coeficiente_de_T<=0 or variacion_de_T<=10)

#WHILE
#MIENTRAS LOS DATOS DE LA RESISTENCIA ELECTRICA SEAN INVALIDOS ENTRAN EN EL WHILE
while(resistencia_invalidad==True):
    print("DATOS DE LA RESISTENCIA ELECTRICA INVALIDOS:Ingrese nuevamente los datos:")
    resistencia_inicial=float(input("INGRESE LA RESISTENCIA:"))
    coeficiente_de_T=float(input("INGRESE EL COEFICIENTE DE TEMPERATURA:"))
    variacion_de_T=float(input("INGRESE LA VARIACION DE TEMPERATURA:"))
    resistencia_invalidad=(resistencia_inicial<=10 or coeficiente_de_T<=0 or variacion_de_T<=-1)
#fin_while
print("FIN DEL BUCLE")
resistencia_final=resistencia_inicial+resistencia_inicial*coeficiente_de_T*variacion_de_T

#OUTPUT
print("")
print("#########################################################")
print("#                 RESISTENCIA ELECTRICA                 #")
print("#########################################################")
print("# RESISTENCIA INICIAL:        ",resistencia_inicial,"ohm ")
print("# COEFICIENTE DE TEMPERATURA: ",coeficiente_de_T,"       ")
print("# VARIACION DE TEMPERATURA:   ",variacion_de_T,"c        ")
print("# RESISTENCIA FINAL:          ",resistencia_final,"w     ")
print("#########################################################")
