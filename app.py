import random

def jogo():
    imprime_menu_principal()
    opcao = 0

    while opcao != 4:
        opcao = int(input("\nEscolha o modo de jogo: \n> "))
        match opcao:
            case 1:
                opcao = 1
                modo_jogador()
            case 2:
                opcao = 2
                modo_facil()
            case 3:
                opcao = 3
                modo_dificil()
            case 4:
                opcao = 4
                break
            case _:
                continue
        imprime_menu_principal()

# Funcoes de impressao:
def imprime_menu_principal():
    print("\n----Menu----\n")
    print("1. Jogar contra um amigo" +
            "\n2. Jogar contra a máquina - FÁCIL" +
            "\n3. Jogar contra a máquina - DIFÍCIL" + 
            "\n4. Sair")

def imprimir_tabuleiro(matriz):
    # Essa linha printa as coordenadas das colunas
    print("\3\t1\t2\t3\n")
    # E aqui iteramos sobre as linhas
    for index_linha, linha in enumerate(matriz):
        # Printa as coordenadas das linhas (O "end" so printa um dois pontos 
        # seguido de um espacamento. Definir o "end" também é importante pra que
        # ele nao pule para uma proxima linha)
        print(index_linha + 1, end=":\t")
        for item in linha:
            # Mapeia os valores da matriz para simbolos conhecidos
            match item:
                case 1:
                    simbolo = "X"
                case -1:
                    simbolo = "O"
                case _:
                    simbolo = "_"

            print(simbolo, end="\t")
        print('\n')

def imprime_pontuacao(jogadores):
    jogador_1 = jogadores[0]
    jogador_2 = jogadores[1]

    print("\n----Pontuacao----")
    # Imprime nome dos jogadores com o espacamento tabulado
    print(f"\6\t{jogador_1["nome"]}\t{jogador_2["nome"]}")
    # Imprime vitorias como X
    print(f"X\t{jogador_1["vitorias_x"]}\t{jogador_2["vitorias_x"]}")
    # Imprime vitorias como O
    print(f"O\t{jogador_1["vitorias_o"]}\t{jogador_2["vitorias_o"]}")
    # Imprime empates
    print(f"----{jogador_1["empates"]} Empates(s)----\n")

# Funcoes Modo de Jogo
def modo_jogador():
    jogadores = []
    continuar_jogo = True

    while continuar_jogo:
        matriz = inicializar_tabuleiro()
        jogadores = inicializa_jogadores(jogadores)
        tem_rounds_restantes = True

        while tem_rounds_restantes:
            # Permite fazer um loop de sequencia entre os jogadores e retornar 
            # para o mesmo jogador caso a jogada seja invalida
            for jogador in jogadores:
                imprimir_tabuleiro(matriz)
                # A jogada retorna um boolean para o estado, caso tenha sido 
                # realizada com sucesso, retorna True, ao contrario, False
                jogada_realizada = jogada_usuario(matriz, jogador)

                if not jogada_realizada:
                    break

                deu_velha = verifica_velha(matriz)
                if deu_velha:
                    tem_rounds_restantes = False
                    jogadores[0]["empates"] += 1
                    jogadores[1]["empates"] += 1
                    print("\n---- Empate! ----\n")
                    break;

                vencedor = verifica_vencedor(matriz)
                if vencedor != 0:
                    tem_rounds_restantes = False
                    # Pega a chave correta pro simbolo atual do jogador, um truque simples que foi possivel pelo jeito que eu
                    # inicializei os jogadores :)
                    chave_dicionario = "vitorias_" + jogador["simbolo"].lower()
                    jogador[chave_dicionario] += 1
                    print(f"\n---- {jogador["nome"]} venceu a rodada! ----\n")
                    break

        imprime_pontuacao(jogadores)
        opcao = int(input("Deseja continuar jogando? \n1. Sim \n2. Não \n> "))
        if opcao == 1:
            continuar_jogo = True
        else:
            continuar_jogo = False

def modo_facil():
    jogadores = []
    continuar_jogo = True

    while continuar_jogo:
        matriz = inicializar_tabuleiro()
        jogadores = inicializa_jogadores(jogadores, "jogador-maquina")
        tem_rounds_restantes = True

        while tem_rounds_restantes:
            for jogador in jogadores:
                imprimir_tabuleiro(matriz)
                # Verificacoes ternarias no Python sao esquisitas, mas basicamente 
                # estamos verificando se o jogador e um humano "tipo jogador" ou
                # maquina e chamando a funcao apropriada.
                jogada_realizada = jogada_usuario(matriz, jogador) if jogador["tipo"] == "jogador" else jogada_maquina_facil(matriz, jogador)

                if not jogada_realizada:
                    break

                deu_velha = verifica_velha(matriz)
                if deu_velha:
                    tem_rounds_restantes = False
                    jogadores[0]["empates"] += 1
                    jogadores[1]["empates"] += 1
                    print("\n---- Empate! ----\n")
                    break;

                vencedor = verifica_vencedor(matriz)
                if vencedor != 0:
                    tem_rounds_restantes = False
                    # Pega a chave correta pro simbolo atual do jogador
                    chave_dicionario = "vitorias_" + jogador["simbolo"].lower()
                    jogador[chave_dicionario] += 1
                    print(f"\n---- {jogador["nome"]} venceu a rodada! ----\n")
                    break

        imprime_pontuacao(jogadores)
        opcao = int(input("Deseja continuar jogando? \n1. Sim \n2. Não \n> "))
        if opcao == 1:
            continuar_jogo = True
        else:
            continuar_jogo = False

def modo_dificil():
    # Basicamente a mesma coisa que o modo_facil mas com uma chamada para a funcao de jogada dificl.
    jogadores = []
    continuar_jogo = True

    while continuar_jogo:
        matriz = inicializar_tabuleiro()
        jogadores = inicializa_jogadores(jogadores, "jogador-maquina")
        tem_rounds_restantes = True

        while tem_rounds_restantes:
            for jogador in jogadores:
                imprimir_tabuleiro(matriz)
                jogada_realizada = jogada_usuario(matriz, jogador) if jogador["tipo"] == "jogador" else jogada_maquina_dificl(matriz, jogador)

                if not jogada_realizada:
                    break

                deu_velha = verifica_velha(matriz)
                if deu_velha:
                    tem_rounds_restantes = False
                    jogadores[0]["empates"] += 1
                    jogadores[1]["empates"] += 1
                    print("\n---- Empate! ----\n")
                    break;

                vencedor = verifica_vencedor(matriz)
                if vencedor != 0:
                    tem_rounds_restantes = False
                    # Pega a chave correta pro simbolo atual do jogador
                    chave_dicionario = "vitorias_" + jogador["simbolo"].lower()
                    jogador[chave_dicionario] += 1
                    print(f"\n---- {jogador["nome"]} venceu a rodada! ----\n")
                    break

        imprime_pontuacao(jogadores)
        opcao = int(input("Deseja continuar jogando? \n1. Sim \n2. Não \n> "))
        if opcao == 1:
            continuar_jogo = True
        else:
            continuar_jogo = False

# Funcoes de Jogada:
def jogada_usuario(matriz, jogador):
    print(f"\n---- {jogador["nome"]}({jogador["simbolo"]}) jogando ----\n")
    linha = leia_coordenada_linha()
    coluna = leia_coordenada_coluna()
    # Posicao retorna true caso seja valida 
    posicao = posicao_valida(matriz, linha, coluna)

    # Realiza jogada caso a posicao seja valida
    if posicao:
        jogar(matriz, jogador["simbolo"], posicao)
        return True
    
    return False

def jogada_maquina_facil(matriz, maquina):
    print(f"\n---- Máquina({maquina["simbolo"]}) jogando ----\n")
    coordenadas = None

    # Roda o loop enquanto nao tiver uma coordenada
    while not coordenadas:
        # Gera valores aleatorios para a linha e coluna e confirma se e valida.
        linha, coluna =  (random.randint(1, 3), random.randint(1, 3))
        coordenada_valida = posicao_valida(matriz, linha, coluna)

        # Atribui a posicao valida a coordenada
        if coordenada_valida:
            coordenadas = coordenada_valida
            break
    
    jogar(matriz, maquina["simbolo"], coordenadas)
    print(f"\n---- Máquina jogou em linha {linha + 1} e coluna {coluna + 1} ----\n")
    return True

def jogada_maquina_dificl(matriz, maquina):
    print(f"\n---- Máquina({maquina["simbolo"]}) jogando ----\n")

    # Verifica se o meio esta livre e joga nele caso esteja.
    if posicao_valida(matriz, 1, 1):
        jogar(matriz, maquina["simbolo"], (1,1))
        print("---- Maquina jogou em linha 2 coluna 2 ----")
        return True
    
    # Verifica se existe uma posicao para a vitoria, e caso exista joga nela
    coordenada_ataque = coordenada_vitoria(matriz, maquina["simbolo"])
    if coordenada_ataque:
        jogar(matriz, maquina["simbolo"], coordenada_ataque)
        print(f"\n---- Máquina jogou em linha {coordenada_ataque[0] + 1} e coluna {coordenada_ataque[1] + 1} ----\n")
        return True

    # Verifica se existe uma posicao que evite a vitoria do adversario, e caso exista joga nela
    simbolo_oponente = "X" if maquina["simbolo"] == "O" else "O"
    coordenada_defesa = coordenada_vitoria(matriz, simbolo_oponente )
    if coordenada_defesa:
        jogar(matriz, maquina["simbolo"], coordenada_defesa)
        print(f"\n---- Máquina jogou em linha {coordenada_defesa[0] + 1} e coluna {coordenada_defesa[1] + 1} ----\n")
        return True
    
    # Verifica cantos disponiveis e joga caso encontre um
    for (linha, coluna) in [(0, 0), (0, 2), (2, 0), (2, 2)]:
        if posicao_valida(matriz, linha, coluna):
            jogar(matriz, maquina["simbolo"], (linha, coluna))
            print(f"\n---- Máquina jogou em linha {linha + 1} e coluna {coluna + 1} ----\n")
            return True
    
    # Verifica bordas disponiveis e joga caso encontre um
    for (linha, coluna) in [(0, 1), (1, 0), (1, 2), (2, 1)]:
        if posicao_valida(matriz, linha, coluna):
            jogar(matriz, maquina["simbolo"], (linha, coluna))
            print(f"\n---- Máquina jogou em linha {linha + 1} e coluna {coluna + 1} ----\n")
            return True
        
def leia_coordenada_linha():
  return int(input("Escolha a linha: (1, 2 ou 3) \n> ")) - 1

def leia_coordenada_coluna():
  return int(input("Escolha a coluna: (1, 2 ou 3) \n> ")) - 1

def jogar(matriz, simbolo, coordenadas):
    # Coordenadas eh "desconstruído", passando os valores linha e coluna
    linha, coluna = coordenadas
    # Baseado com a escolha do jogador, símbolo é atribuído à matriz
    matriz[linha][coluna] = 1 if simbolo == "X" else -1

def coordenada_vitoria(matriz, simbolo):
    # Usaremos mais na frente para evitar repeticoes de ifs
    valor = 1 if "X" == simbolo else -1

    soma_diagonal = 0
    soma_diagonal_inversa = 0

    # Aqui fazemos mais ou menos a mesma cosa que na verificacao de vitoria, mas
    # olhamos para os casos em que falta 1 valor para a vitoria (2 e -2)
    for index_linha in range(len(matriz)):
        soma_linha = sum(matriz[index_linha])
        soma_coluna = matriz[0][index_linha] + matriz[1][index_linha] + matriz[2][index_linha]

        # Quando encontramos esses casos (nesse If seria uma linha) nos verificamos
        # qual e o espaco vazio que nos garantia a vitoria e retornamos ele.
        if soma_linha == 2 * valor:
            for index_coluna in range(len(matriz[index_linha])):
                if matriz[index_linha][index_coluna] == 0:
                    return (index_linha, index_coluna)
        
        if soma_coluna == 2 * valor:
            for index_coluna in range(len(matriz[index_linha])):
                if matriz[index_coluna][index_linha] == 0:
                    return (index_coluna, index_linha)

        soma_diagonal += matriz[index_linha][index_linha]
        soma_diagonal_inversa += matriz[index_linha][(len(matriz) - 1) - index_linha]

    if soma_diagonal == 2 * valor:
        for index_linha in range(len(matriz)):
            if matriz[index_linha][index_linha] == 0:
                return (index_linha, index_linha)
    
    if soma_diagonal_inversa == 2 * valor:
        for index_linha in range(len(matriz)):
            index_complementar = (len(matriz[index_linha]) - 1) - index_linha
            if matriz[index_linha][index_complementar] == 0:
                return (index_linha, index_complementar)

# Funcoes de inicializacao:
def inicializa_jogadores(jogadores, modo = "jogador-jogador"):
    # Inverte o simbolo dos jogadores caso eles ja existam e inverte a ordem dos playes, se não os cria
    if jogadores:
        jogadores[0]["simbolo"], jogadores[1]["simbolo"] = jogadores[1]["simbolo"], jogadores[0]["simbolo"]
        jogadores[0], jogadores[1] = jogadores[1], jogadores[0]
        return jogadores
    
    nome_jogador_1 = input("Insira o seu nome (Jogador X): \n> ")
    if modo == "jogador-jogador":
        nome_jogador_2 = input("Insira o seu nome (Jogador O): \n> ")
    else:
        nome_jogador_2 = "Máquina"

    # Aqui colocamos um tipo jogador ou jogador-maquina para sabermos nas funcoes de modo maquina se devemos pedir um input
    # do usuario ou chamar a funcao apropriada da maquina
    jogador_1 = {"nome": nome_jogador_1, "simbolo": "X", "vitorias_x": 0, "vitorias_o": 0, "empates": 0, "tipo": "jogador"}
    jogador_2 = {"nome": nome_jogador_2, "simbolo": "O", "vitorias_x": 0, "vitorias_o": 0, "empates": 0, "tipo": "jogador" if modo == "jogador-jogador" else "jogador-maquina"}

    return [jogador_1, jogador_2]

def inicializar_tabuleiro():
  matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
  return matriz

# Funcoes de validacao:
def posicao_valida(matriz, linha, coluna):
  # Verifica se as coordenadas escolhidas são válidas na matriz (não ultrapassam o tamanho da matriz)
  if 0 <= linha <= 2 and 0 <= coluna <= 2:
    # Se não houver "X" ou "O" na posição escolhida da matriz ele retorna uma 
    # tupla com as coordenadas da jogada, que são usadas na função "jogar"
    if matriz[linha][coluna] not in [-1, 1]:
      return (linha, coluna)
  return None

# Funcoes de verificacao de vitoria:
def verifica_velha(matriz):
    resultado = verifica_vencedor(matriz)
    # Verifica se já houve algum ganhador para não entrar no loop da velha
    if resultado != 0:
        return False
    
    # Verifica se há 0 na matriz, se não, houve empate (True)
    for linha in matriz:
        if 0 in linha:
            return False
      
    return True
    
def verifica_vencedor(matriz):
    # Valor de vitoria e sempre igual a 3 vezes o valor do simbolo
    # X: 1
    # O: -1
    soma_diagonal = 0
    soma_diagonal_inversa = 0

    for index_linha in range(len(matriz)):
        soma_linha = sum(matriz[index_linha])
        # Tinhamos criado uma amtrix transposta para fazer esse calculo antes, mas como e so um jogo da velha, acho que 
        # podemos deixar os valores harcoded aqui. (Nao gosto de for dentro de for)
        soma_coluna = matriz[0][index_linha] + matriz[1][index_linha] + matriz[2][index_linha]

        if soma_linha == 3 or soma_coluna == 3:
            return 1
        elif soma_linha == -3 or soma_coluna == -3:
            return -1

        # O indice da linha da diagonal e igual ao index da coluna, entao pode mos fazer assim:
        soma_diagonal += matriz[index_linha][index_linha]
        # Ja o index da coluna da diagonal inversa e sempre um "complemento" da normal, entao podemos subtrair o index 
        # da linha(mesmo da coluna no caso de diagonais) do index maximo de coluna para obter esse complemento
        soma_diagonal_inversa += matriz[index_linha][(len(matriz) - 1) - index_linha]

    if soma_diagonal == 3 or soma_diagonal_inversa == 3:
        return 1
    elif soma_diagonal == -3 or soma_diagonal_inversa == -3:
        return -1
    
    return 0

jogo()
