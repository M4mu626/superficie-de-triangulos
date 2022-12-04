n=int(input("Cuantos triángulos procesará:"))
equilatero=0
isosceles=0
escaleno=0

for x in range(n):
    lado1=int(input("Ingrese el valor del lado 1:"))
    lado2=int(input("Ingrese el valor del lado 2:"))
    lado3=int(input("Ingrese el valor del lado 3:"))
    if lado1==lado2 and lado1==lado3:
        print("Este triangulo es equilatero")
        equilatero=equilatero+1
    else:
        if lado1==lado2 or lado1==lado3 or lado2==lado3:
            print("Este triangulo es isosceles")
            isosceles=isosceles+1
        else:
            print("Este triangulo es escaleno")
            escaleno=escaleno+1
        
print("La cantidad de triángulos equilateros son")
print(equilatero)
print("La cantidad de triángulos isosceles son")
print(isosceles)
print("La cantidad de triángulos escalenos son")
print(escaleno)

input()


""" Realizar un programa que lea los lados de n triángulos, e informar:
a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
b) Cantidad de triángulos de cada tipo.""" 
