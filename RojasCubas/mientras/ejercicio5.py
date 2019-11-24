import os
#COMPROBACION DE UNA FECHA
print("")
#declararación de variables
numero_del_dia,nombre_del_dia,mes,anio,fecha,nombre_del_dia_invalido,numero_del_dia_invalido,anio_invalido=0,"","",0,"",False,False,False

#input
nombre_del_dia=(os.sys.argv[1]).lower()
numero_del_dia=int(os.sys.argv[2])
mes=os.sys.argv[3].lower()
anio=int(os.sys.argv[4])

#processing
#verificador de el valor del dia,mes y año
nombre_del_dia_invalido=((nombre_del_dia!="lunes") and (nombre_del_dia!="martes") and (nombre_del_dia!="miercoles") and (nombre_del_dia!="jueves") and (nombre_del_dia!="viernes") and (nombre_del_dia!="sabado") and (nombre_del_dia!="viernes"))
numero_del_dia_invalido=(numero_del_dia<0 or numero_del_dia>32)
mes_invalido=((mes!="enero") and (mes!="febrero") and (mes!="marzo") and (mes!="abril") and (mes!="mayo") and (mes!="junio") and (mes!="julio") and (mes!="agosto") and (mes!="setiembre") and (mes!="octubre") and (mes!="noviembre") and (mes!="diciembre"))
anio_invalido=(anio<1582 or anio>2019)

#mientras el nombre del dia es inválido mostrar un mensaje de error y pedir nuevamente el nombre del dia
while(nombre_del_dia_invalido==True):
    print("NOMBRE DEL DÍA INVÁLIDO")
    nombre_del_dia=input("ingrese nombre del día:")
    nombre_del_dia_invalido=((nombre_del_dia!="lunes") and (nombre_del_dia!="martes") and (nombre_del_dia!="miercoles") and (nombre_del_dia!="jueves") and (nombre_del_dia!="viernes") and (nombre_del_dia!="sabado") and (nombre_del_dia!="viernes"))
#fin_while

#mientras el número del dia es inválido mostrar un mensaje de error y pedir nuevamente el número del dia
while(numero_del_dia==True):
    print("NUMERO DEL DÍA INVALIDO")
    numero_del_dia=int(input("ingrese número del día:"))
    numero_del_dia_invalido=(numero_del_dia<0 or numero_del_dia>32)
#fin_while

#mientras el mes sea invalido mostrar un mensaje de error y pedir nuevamente el mes
while(mes_invalido==True):
    print("EL MES ES INVÁLDO")
    mes=input("ingrese el mes:")
    mes_invalido=((mes!="enero") and (mes!="febrero") and (mes!="marzo") and (mes!="abril") and (mes!="mayo") and (mes!="junio") and (mes!="julio") and (mes!="agosto") and (mes!="setiembre") and (mes!="octubre") and (mes!="noviembre") and (mes!="diciembre"))
#fin_while

#mientras el año se invalido mostrar un mensaje de error y pedir nuevamente el año
while(anio_invalido==True):
    print("AÑO INVÁLIDO")
    print("NO INGRESE UN AÑO MENOR A 1582 Y MAYOR A 2019")
    anio=int(input("ingrese año:"))
    anio_invalido=(anio<1582 or anio>2019)
#fin_while

fecha=nombre_del_dia+" "+str(numero_del_dia)+" de "+mes+" del "+str(anio)
#output
print("bucle concluido!")
print("DATOS INGRESADOS VÁLIDOS")
print("MOSTRANDO LOS DATOS...")
print("**************************************")
print("*          VALOR DE LA FECHA         *")
print("**************************************")
print("*NOBRE DEL DÍA:",nombre_del_dia,"               *")
print("NÚMERO DEL DÍA:",numero_del_dia,"                   *")
print("*MES:",mes,"                         *")
print("*AÑO:",anio,"                          *")
print("*FECHA:",fecha,"    *")
print("**************************************")


