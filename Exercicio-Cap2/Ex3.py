flag = 1
while flag == 1:
    entrada = input("sexo(M ou F): ")
    if entrada != "M" and entrada != "F":
        print("Invalido")
    else:
        flag = 0