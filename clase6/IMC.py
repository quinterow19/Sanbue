# hola comunidad
peso = float(input("Introduce tu peso en kilogramos: "))
altura = float(input("Introduce tu altura en metros: "))

# float: decimal
# print(f"El peso ingresado es: {peso}")
# print(f"El altura ingresado es: {altura}")

# Cálculo del IMC
imc = peso / (altura ** 2)

# Mostrar resultado
print(f"Tu IMC es: {round(imc, 2)}")
#round= redondear