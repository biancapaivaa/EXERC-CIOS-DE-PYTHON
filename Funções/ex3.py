# Exercício 3 - Bianca Paiva

def par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
    
num = int(input("Digite um número para verificar se é par ou ímpar: "))
print(f"O número {num} é {par_ou_impar(num)}.")