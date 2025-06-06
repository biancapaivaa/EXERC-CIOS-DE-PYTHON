# Exercício 4 - Bianca Paiva

def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

num_fat = int(input("Digite um número para calcular o fatorial: "))
print(f"O fatorial de {num_fat} é {fatorial(num_fat)}.")