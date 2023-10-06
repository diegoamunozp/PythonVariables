DistanciaMT = float(input("Ingrese una distancia (Metros): "))

print("Elija la opcion a la que quiere hacer la conversion:")
print("1 - Kilómetros  (Km)")
print("2 - Milímetros  (Mm)")
print("3 - Centímetros (Cm)")

opcion = int(
    input("Ingrese el número de la unidad de medida deseada (1/2/3): "))


if opcion == 1:
    
    DistanciaKM = DistanciaMT / 1000
    print(f"{DistanciaMT} metros equivalen a {DistanciaKM} kilómetros.")
    
elif opcion == 2:
    DistanciaMM = DistanciaMT * 1000
    print(f"{DistanciaMT} metros equivalen a {DistanciaMM} milímetros.")
    
elif opcion == 3:

    DistanciaCM = DistanciaMT * 100
    print(f"{DistanciaMT} metros equivalen a {DistanciaCM} centímetros.")
    
else:
    print("Elijio una opcion incorrecta, intentelo nuevamente (1-3)")