import os
#promedio de 4 notas del curso de Historia
print("")
#declararación de variables
nota1,nota2,nota3,nota4,promedio,notas_invalidas,a=0.0,0.0,0.0,0.0,0.0,False,""

#input
nota1=float(os.sys.argv[1])
nota2=float(os.sys.argv[2])
nota3=float(os.sys.argv[3])
nota4=float(os.sys.argv[4])

#processing
notas_invalidas=((nota1<=0 or nota1>20) or (nota2<=0 or nota2>20) or (nota3<=0 or nota3>20) or (nota4<=0 or nota4>20))       #verificar las notas

#mientras la notas_invaldas sea verdadera mostrar un mensaje y pedir nuevamente las ntas

while(notas_invalidas==True):       #mientras la notas_validas se igual a verdareo hacer:
    print("nota ingresada invalida!,Ingrese nuevamente sus Notas")
    nota1=float(input("ingrese nota1:"))
    nota2=float(input("ingrese nota2:"))
    nota3=float(input("ingrese nota3:"))
    nota4=float(input("ingrese nota4:"))
    notas_invalidas=((nota1<=0 or nota1>20) or (nota2<=0 or nota2>20) or (nota3<=0 or nota3>20) or (nota4<=0 or nota4>20))

#fin_while
promedio=(nota1+nota2+nota3+nota4)/4

#output
print("")
print("bucle concluido!")
print("Notas ingresadas correctas")
print("calculando el promedio...")

#condicion si el promedio es mayor o igual que 10.5  mostrar alumno aaprobado sino mostrar alumno desaprobado
if(promedio>10.5):
    a="ALUMNO APROBADO"
else:
    a="ALUMNO DESAPROBADO"
#fin_if
print("**************************************")
print("*       PROMEDIO DE HISTORIA         *")
print("**************************************")
print("*NOTA1:",nota1,"                        *")
print("*NOTA2:",nota2,"                        *")
print("*NOTA3:",nota3,"                        *")
print("*NOTA4:",nota4,"                        *")
print("*PROMEDIO:",promedio,"                     *")
print("**************************************")
print(a)
print("**************************************")
