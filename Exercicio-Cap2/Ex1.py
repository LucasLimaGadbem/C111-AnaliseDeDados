name = input("Seu nome completo: ")
up = name.upper()
print(up)
lo = name.lower()
print(lo)
print("Como contar?")
print("1 - contar espaco")
print("2 - nao contar espaco")
'separa os nomes'
partes = name.split()
op = int(input())
if op == 1:
    qtd = len(name)
    print(qtd)
elif op == 2:
    'junta sem os espacos'
    junto = "".join(partes)
    number = len(junto)
    print(number)
else:
    print("Invalida")
'o :-1 eh para pegar ate o penultimo nome'
new = partes[:-1] + ["do Inatel"]
out = " ".join(new)
print(out)