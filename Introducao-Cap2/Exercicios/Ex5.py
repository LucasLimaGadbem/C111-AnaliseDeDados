numero = int(input("Valor entre 1000 e 9999: "))
while 1000 > numero or 9999 < numero:
    print("Valor invalido")
    numero = int(input("Valor entre 1000 e 9999: "))

#// é divisao inteira
unidade = numero % 10
dezena = (numero % 100) // 10
centena = (numero % 1000) // 100
milhar = numero // 1000

print(f"Unidade: {unidade}")
print(f"Dezena: {dezena}")
print(f"Centena: {centena}")
print(f"Milhar: {milhar}")