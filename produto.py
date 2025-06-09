# Lista para armazenar os produtos
estoque = []

# Função para adicionar um produto
def adicionar_produto():
    nome = input("Digite o nome do produto: ").strip()
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade em estoque: "))
    
    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }
    estoque.append(produto)
    print(f"Produto '{nome}' adicionado com sucesso!\n")

# Função para buscar um produto pelo nome
def buscar_produto():
    nome_busca = input("Digite o nome do produto que deseja buscar: ").strip().lower()
    encontrado = False
    for produto in estoque:
        if produto["nome"].lower() == nome_busca:
            print(f"\nProduto encontrado:")
            print(f"Nome: {produto['nome']}")
            print(f"Preço: R${produto['preco']:.2f}")
            print(f"Quantidade em estoque: {produto['quantidade']}\n")
            encontrado = True
            break
    if not encontrado:
        print("Produto não encontrado.\n")

# Função para atualizar o estoque de um produto
def atualizar_estoque():
    nome_busca = input("Digite o nome do produto que deseja atualizar: ").strip().lower()
    for produto in estoque:
        if produto["nome"].lower() == nome_busca:
            nova_quantidade = int(input(f"Digite a nova quantidade em estoque para '{produto['nome']}': "))
            produto["quantidade"] = nova_quantidade
            print(f"Estoque de '{produto['nome']}' atualizado com sucesso!\n")
            return
    print("Produto não encontrado.\n")

# Função para listar todos os produtos
def listar_produtos():
    if not estoque:
        print("Nenhum produto cadastrado.\n")
    else:
        print("\n--- Lista de Produtos ---")
        for produto in estoque:
            print(f"Nome: {produto['nome']}")
            print(f"Preço: R${produto['preco']:.2f}")
            print(f"Quantidade: {produto['quantidade']}")
            print("------------------------")
        print()

# Função principal com menu
def main():
    while True:
        print("===== MENU DO SISTEMA DE ESTOQUE =====")
        print("1 - Adicionar produto")
        print("2 - Buscar produto")
        print("3 - Atualizar estoque")
        print("4 - Listar produtos")
        print("5 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_produto()
        elif escolha == "2":
            buscar_produto()
        elif escolha == "3":
            atualizar_estoque()
        elif escolha == "4":
            listar_produtos()
        elif escolha == "5":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Executar o programa
if __name__ == "__main__":
    main()
