Sec = int(input("Ingrese un tiempo en segundos: "))

Hour = Sec // 3600  
SecResta = Sec % 3600
minutos = SecResta // 60  
SecFinal = SecResta % 60


print(f"{Sec} segundos equivalen a {Hour} hora/s, {minutos} minuto/s y {SecFinal} segundo/s.")
