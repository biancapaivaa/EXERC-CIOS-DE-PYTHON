# Exercício 9 - Bianca Paiva

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")
if operacao == "+":
    print(f"Resultado: {n1 + n2}")
elif operacao == "-":
    print(f"Resultado: {n1 - n2}")
elif operacao == "*":
    print(f"Resultado: {n1 * n2}")
elif operacao == "/":
    if n2 != 0:
        print(f"Resultado: {n1 / n2}")
    else:
        print("Erro: divisão por zero.")
else:
    print("Operação inválida.")
print("-" * 30)