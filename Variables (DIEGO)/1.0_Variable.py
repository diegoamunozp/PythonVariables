print("Hola we\n")
salarioD = int(input("Ingrese su salario diario: "))
DiasT = int(input("Ingrese los dias trabajados: "))

total1 = salarioD * DiasT
pension = total1 * 0.10
salud = total1 * 0.15

total2 = total1 - pension - salud

print(f"El salario total es: {total1}\nEl salario descontando Concepto por pension y salud es: {total2}")