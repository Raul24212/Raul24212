while True:
    numero = input("Puntuacion de Calificaciones") 
    if(numero == "salir"):
        break
    if(int(numero) > 0 and int (numero) < 10):
        print("sobresaliente") 
    elif(int(numero) > 5  and int (numero) < 10):
        print("Notable")
    elif(int(numero)> 99 and int(numero) < 100):
        print("suficiente")
    else:
        print("Insuficiente") 