#REPETITIVAS MIENTRAS QUE CALCULA LA FORMULA DE LA HIDROSTATICA
import os
densidad_liquido,gravedad,Altura=0.0,0.0,0.0

#ARGUMENTOS
densidad_liquido=float(os.sys.argv[1])
gravedad=float(os.sys.argv[2])
Altura=float(os.sys.argv[3])

#PROCESSING
precion_invalidad=(densidad_liquido<=0 or gravedad<=0 or Altura<=0)

#WHILE
#MIENTRAS LOS DATOS DE LA P.HIDROSTATICA SEAN INCORECTOS ENTRAN EN EL WHILE
while(precion_invalidad==True):
    print("DATOS INVALIDOS DE LA P. HIDROSTATICA:Ingrese nuevamente los datos")
    densidad_liquido=float(input("INGRESE LA DENSIDAD DEL LIQUIDO:"))
    gravedad=float(input("INGRESE LA GRAVEDAD:"))
    Altura=float(input("INGRESE LA ALTURA:"))
    precion_invalidad=(densidad_liquido<=0 or gravedad<=0 or Altura<=0)
#fin_while
print("FIN DEL BUCLE")
precion_hidrostatica=densidad_liquido*gravedad*Altura

#OUTPUT
print("")
print("#####################################################")
print("#         HALLA LA PRECION HIDROSTATICA             #")
print("#####################################################")
print("# DENSIDAD DEL LIQUIDO: ",densidad_liquido,"kg/m.m.m ")
print("# GRAVEDAD:             ",gravedad,"m/s.s            ")
print("# ALTURA:               ",Altura,"m                  ")
print("# PRECION HIDROSTATICA: ",precion_hidrostatica,"     ")
print("#####################################################")

