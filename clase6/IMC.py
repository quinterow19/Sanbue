peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = peso / (altura ** 2)

print(f"\nIMC: {round(imc,2)}")

if imc < 18.5:
    print("IMC BAJO (menor al normal)")
elif imc <= 24.9:
    print("IMC NORMAL")
elif imc <= 29.9:
    print("IMC ALTO (mayor al normal)")
else:
    print("IMC MUY ALTO (obesidad)")