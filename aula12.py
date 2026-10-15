import json


def carregar_dados():
    try:
        with open("jogadores.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except:
        return []


def salvar_dados(jogadores):
    with open("jogadores.json", "w", encoding="utf-8") as arquivo:
        json.dump(jogadores, arquivo, indent=4, ensure_ascii=False)


def cadastrar_jogador():
    jogadores = carregar_dados()
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    pontuacao = int(input("Pontuação: "))
    jogador = {"nome": nome, "idade": idade, "pontuacao": pontuacao}
    jogadores.append(jogador)
    salvar_dados(jogadores)
    print("Jogador cadastrado com sucesso!")


def ver_jogadores():
    jogadores = carregar_dados()
    print("\n=== JOGADORES ===")
    if len(jogadores) == 0:
        print("Nenhum jogador cadastrado.")
        return
    for jogador in jogadores:
        print(f"{jogador['nome']} - {jogador['pontuacao']}")


def ver_ranking():
    jogadores = carregar_dados()
    jogadores.sort(key=lambda x: x["pontuacao"], reverse=True)
    print("\n=== RANKING ===")
    posicao = 1
    for jogador in jogadores:
        print(f"{posicao} - {jogador['nome']} - {jogador['pontuacao']}")
        posicao += 1


def gerar_relatorio():
    jogadores = carregar_dados()
    total_pontos = 0
    maior_pontuacao = 0
    melhor_jogador = ""
    for jogador in jogadores:
        pontos = jogador["pontuacao"]
        total_pontos += pontos
        if pontos > maior_pontuacao:
            maior_pontuacao = pontos
            melhor_jogador = jogador["nome"]
    media = total_pontos / len(jogadores)
    print("\n=== RELATÓRIO ===")
    print(f"Total de jogadores: {len(jogadores)}")
    print(f"Média de pontuação: {media:.2f}")
    print(f"Melhor jogador: {melhor_jogador}")
    print(f"Maior pontuação: {maior_pontuacao}")


def definir_nivel(pontuacao):
    if pontuacao < 50:
        return "Bronze"
    elif pontuacao < 80:
        return "Prata"
    else:
        return "Ouro"


def buscar_jogador():
    nome_busca = input("Digite o nome do jogador: ")
    jogadores = carregar_dados()
    encontrado = False
    for jogador in jogadores:
        if jogador["nome"].lower() == nome_busca.lower():
            print("\n=== JOGADOR ENCONTRADO ===")
            print(f"Nome: {jogador['nome']}")
            print(f"Idade: {jogador['idade']}")
            print(f"Pontuação: {jogador['pontuacao']}")
            print(f"Nível: {definir_nivel(jogador['pontuacao'])}")
            encontrado = True
    if not encontrado:
        print("Jogador não encontrado.")


while True:
    print("\n=== SISTEMA DE JOGADORES ===")
    print("1 - Cadastrar jogador")
    print("2 - Ver jogadores")
    print("3 - Ver ranking")
    print("4 - Ver relatório")
    print("5 - Buscar Jogador")
    print("6 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_jogador()
    elif opcao == "2":
        ver_jogadores()
    elif opcao == "3":
        ver_ranking()
    elif opcao == "4":
        gerar_relatorio()
    elif opcao == "5":
        buscar_jogador()
    elif opcao == "6":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida!")
