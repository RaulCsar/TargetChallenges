entrada = input("Insira uma palavra a ser invertida: ")
lista = []
atsil = []
for e in entrada:
    lista.append(e)
while len(lista)!=0:
    for i in range(len(lista)):
        atsil.append(lista.pop())

saida = ""
for letra in atsil:
    saida+=letra
print(f"A palavra invertida é: {saida}.\n")
