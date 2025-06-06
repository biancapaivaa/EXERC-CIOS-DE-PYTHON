# Exercício 5 - Bianca Paiva

def exibir_nomes(lista):
    for nome in lista:
        print(f"Nome: {nome}")

nomes = []
qtd = int(input("Quantos nomes deseja digitar? "))
for i in range(qtd):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)
print("Lista de nomes digitados:")
exibir_nomes(nomes)