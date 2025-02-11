import math as mp

numero = float(input("Entre com um numero: "))
raiz = mp.sqrt(numero)
print(f'raiz do {numero} é {raiz}')
teto = mp.ceil(numero)
print(f'teto do {numero} é {teto}')
chao = mp.floor(numero)
print(f'chao do {numero} é {chao}')
inteira = mp.trunc(numero)
print(f'parte inteira do {numero} é {inteira}')