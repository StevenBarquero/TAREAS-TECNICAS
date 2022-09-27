from operator import truediv
from turtle import fd
menu="""
Menu de operaciones.
1-suma
2-resta
3-multiplicacion
4-division
5-verificacion numero primo
6-verificacion numero palindromo
7-SALIR
"""
numero1= 0
numero2= 0
suma=0
resta=0
primos=0
resultadoprimo=0
resultadopalindromo=0
palindromos=0
multiplicacion=0
division=0
print("Bienvenido a el menu de operaciones")
seguir=True
while(seguir == True):
    print(menu)
    opcion= int(input("cual operacion deseas realizar?"))
    if opcion is 1:
        print("Digite su primer numero")
        numero1=int(input())
        print("Digite el otro numero")
        numero2=int(input())
        suma=numero1+numero2
        print("El resultado de la suma de sus dos numeros es", suma)
    elif opcion is 2:
        print("Digite su primer numero")
        numero1=int(input())
        print("Digite el otro numero")
        numero2=int(input())
        resta=numero1-numero2
        print("El resultado de la resta de sus dos numeros es", resta)
    elif opcion is 3:
        print("Digite su primer numero")
        numero1=int(input())
        print("Digite el otro numero")
        numero2=int(input())
        resta=numero1*numero2
        print("El resultado de la multiplicacion de sus dos numeros es", multiplicacion)    
    elif opcion is 4:
        print("Digite su primer numero")
        numero1=int(input())
        print("Digite el otro numero")
        numero2=int(input())
        resta=numero1/numero2
        print("El resultado de la division de sus dos numeros es", division)
    elif opcion is 5:
        print("Digite su numero para saber si es primo o no")
        numero1=int(input())

        esPrimo=True
        for i in range(2,numero1):
            if numero1%i==0:
                esPrimo=False
                break
            if esPrimo:
                print("el numero que digito SI es un numero primo")
            else:
                print("el numero que digito NO es un numero primo")    
    elif opcion is 6:
        numero1 = input("Digite el numero para saber si es palindromo o no")
        if numero1 == numero1[::-1]:
            print("el numero que digito SI es palindromo")
        else:
            print("el numero que digito NO es palindromo")                
else:
    print("calculadora cerrada")