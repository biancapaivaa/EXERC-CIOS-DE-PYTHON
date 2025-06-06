# Exercício 8 - Bianca Paiva

letra = input("Digite uma letra: ").lower()
if letra in "aeiou":
    print("É uma vogal.")
elif letra.isalpha() and len(letra) == 1:
    print("É uma consoante.")
else:
    print("Não é uma letra válida.")
print("-" * 30)