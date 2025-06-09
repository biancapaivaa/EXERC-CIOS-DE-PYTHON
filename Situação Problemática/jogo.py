# Função para criar um personagem com vida fixa
def criar_personagem(numero):
    print(f"\nCriação do Personagem {numero}:")
    nome = input("Digite o nome do personagem: ")
    forca = int(input(f"Digite a força de ataque de {nome}: "))
    personagem = {
        "nome": nome,
        "vida": 100,  # Vida fixa
        "forca": forca
    }
    print(f"Personagem {nome} criado com sucesso com 100 de vida!\n")
    return personagem

# Função para realizar um ataque entre personagens
def atacar(atacante, defensor):
    if atacante["vida"] <= 0:
        print(f"{atacante['nome']} não pode atacar, pois está derrotado.\n")
        return

    if defensor["vida"] <= 0:
        print(f"{defensor['nome']} já está derrotado.\n")
        return

    dano = atacante["forca"]
    defensor["vida"] -= dano

    print(f"\n{atacante['nome']} atacou {defensor['nome']} causando {dano} de dano!")

    if defensor["vida"] <= 0:
        defensor["vida"] = 0
        print(f"{defensor['nome']} foi derrotado!\n")
    else:
        print(f"{defensor['nome']} agora tem {defensor['vida']} de vida.\n")

# Função para exibir o status de um personagem
def exibir_status(personagem):
    print(f"--- STATUS DE {personagem['nome'].upper()} ---")
    print(f"Vida: {personagem['vida']}")
    print(f"Força: {personagem['forca']}")
    print("----------------------------------\n")

# Código principal
def main():
    jogador1 = criar_personagem(1)
    jogador2 = criar_personagem(2)

    while True:
        print("Escolha uma ação:")
        print(f"1 - {jogador1['nome']} ataca {jogador2['nome']}")
        print(f"2 - {jogador2['nome']} ataca {jogador1['nome']}")
        print("3 - Mostrar status dos personagens")
        print("4 - Encerrar o jogo")
        escolha = input("Digite o número da ação: ")

        if escolha == "1":
            atacar(jogador1, jogador2)
        elif escolha == "2":
            atacar(jogador2, jogador1)
        elif escolha == "3":
            exibir_status(jogador1)
            exibir_status(jogador2)
        elif escolha == "4":
            print("\nJogo encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Executa o programa
if __name__ == "__main__":
    main()
