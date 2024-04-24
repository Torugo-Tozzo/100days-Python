import random

# Função para criar um baralho
def criar_baralho():
    baralho = []
    naipes = ['Copas', 'Ouros', 'Paus', 'Espadas']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei', 'Ás']
    for naipe in naipes:
        for valor in valores:
            baralho.append(f'{valor} de {naipe}')
    random.shuffle(baralho)
    return baralho

# Função para calcular o valor de uma mão
def calcular_valor(mao):
    valor = 0
    as_count = 0
    for carta in mao:
        valor_carta = carta.split()[0]
        if valor_carta in ['Valete', 'Dama', 'Rei']:
            valor += 10
        elif valor_carta == 'Ás':
            valor += 11
            as_count += 1
        else:
            valor += int(valor_carta)
    while valor > 21 and as_count:
        valor -= 10
        as_count -= 1
    return valor

# Função para mostrar as cartas de uma mão
def mostrar_mao(jogador, mao):
    print(f"Mão do {jogador}:")
    for carta in mao:
        print(carta)
    

# Função para o jogo
def blackjack():
    baralho = criar_baralho()
    jogador_mao = [baralho.pop(), baralho.pop()]
    computador_mao = [baralho.pop(), baralho.pop()]
    
    mostrar_mao("Victor", jogador_mao)
    mostrar_mao("Computador: ", [computador_mao[0], 'Carta escondida'])

    while True:
        if calcular_valor(jogador_mao) == 21:
            print("Blackjack!")
            break
        elif calcular_valor(jogador_mao) > 21:
            print("Estourou!")
            break

        opcao = input("Deseja pedir outra carta? (s/n): ").lower()
        if opcao == 's':
            jogador_mao.append(baralho.pop())
            mostrar_mao("Victor", jogador_mao)
        else:
            break

    if calcular_valor(jogador_mao) <= 21:
        while calcular_valor(computador_mao) < 17:
            computador_mao.append(baralho.pop())
        mostrar_mao("Computador", computador_mao)

        jogador_valor = calcular_valor(jogador_mao)
        computador_valor = calcular_valor(computador_mao)

        if jogador_valor > 21 or (computador_valor <= 21 and computador_valor > jogador_valor):
            print("Você perdeu!")
        elif computador_valor > 21 or jogador_valor > computador_valor:
            print("Você ganhou!")
        else:
            print("Empate!")

# Iniciar o jogo
blackjack()