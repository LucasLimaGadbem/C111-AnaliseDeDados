km = int(input("distancia da viagem em km: "))
if km <= 200:
    valor = km * 0.5
else:
    valor = km * 0.45
print(f'Valor da viagem é {valor}')