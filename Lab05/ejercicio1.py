# Tendencia e Innovacion en Tecnologia Agricola (TEA)
secuencia = "x-DSPAM-Confidence:0.85"
inicio = secuencia.find(":") +1
final = len(secuencia) 
numero= float (secuencia [inicio:final]) 
print(numero)
print(inicio, final)
print(type(numero)) 