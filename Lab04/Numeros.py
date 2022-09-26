contador = 0
suma = 0
maximo = 0
minimo = 0
Primernumero = True
while True:
    numero = input("Ingrese un numero: ")
    if (numero == "salir"):
        break
    contador = contador + 1
    suma = suma + int(numero)
    if(Primernumero):
        minimo = int(numero)
        maximo = int(numero)
        Primernumero = False
    else:
        if(int(numero) > maximo):
            maximo = int(numero)
        if(int(numero) < minimo):
            minimo = int(numero)
print("Minimo:", minimo)
print("Maximo:", maximo)