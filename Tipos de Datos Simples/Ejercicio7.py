peso = float(input("Introduce el peso en kg: "))

altura = float(input("Introduce la altura en metros: "))

imc = round(peso/(altura**2))

print("El indice de masa corporal es: " + str(imc))