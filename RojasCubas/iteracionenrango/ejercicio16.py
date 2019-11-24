import os
#mostra el mensaje bienbenido al curso de programación en unrango dado por  el usuario
#input
rango=int(os.sys.argv[1])

#prossecing
#verificador
rango_invalido=(rango<0)
#mientras el rango sea invalido hacer:
while(rango_invalido==True):
    print("RANGO INVÁLIDO")
    rango=int(input("ingrese el rango:"))
    rango_invalido=(rango<0)
#fin_while
#iterar en rango
for i in range(rango):
    print("BIEMBENIDO")
#fin_for_in_range
