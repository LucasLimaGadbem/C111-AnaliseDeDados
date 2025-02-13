print("Numero que voce quer a tabuada")
numero = int(input("numero: "))
comeca = int(input("comeca: "))
termina = int(input("termina: "))
for i in range(comeca, termina+1):
    if comeca <= termina:
        resultado = numero*i
        print(f"{numero} x {i} = {resultado}")
    comeca = comeca + 1