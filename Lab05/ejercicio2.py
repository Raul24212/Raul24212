try:
    entrada = input("Ingrese el nombre del archivo: ") 
    archivo = open(entrada, "r", encoding="UTF=6" ) 
    for line in archivo:
        print(line.upper()) 
except:
    print("Error, archivo no existe")

#print(archivo.read())
