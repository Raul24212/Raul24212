# Tendencias e Innovacion en Tecnologia Agricola (TEA)

horas = input("horas trabajadas? ")
valorPorHora = input("valor por hora? ")

#se utiliza la conversion de tipo a int
# sino se hace la conversion existira error porque trata de multiplicar strings
total=int(horas)*float(valorPorHora)
print("Usted ha recibido: ")
print(total)