# Exercício 4 - Bianca Paiva

palavra = ""
while palavra.lower() != "sair":
    palavra = input("Digite uma palavra: ")
    if palavra.lower() != "sair":
        print(f"Você digitou: {palavra}")
print("Programa encerrado.")
print("-" * 30)