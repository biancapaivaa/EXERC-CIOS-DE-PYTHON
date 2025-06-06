# Exercício 7 - Bianca Paiva

dia = int(input("Digite um número (1 a 7): "))
dias_semana = {
    1: "Domingo",
    2: "Segunda-feira",
    3: "Terça-feira",
    4: "Quarta-feira",
    5: "Quinta-feira",
    6: "Sexta-feira",
    7: "Sábado"
}
print(dias_semana.get(dia, "Número inválido."))
print("-" * 30)